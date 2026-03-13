from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CourseForm
from .models import Course, Enrollment, News
class CourseListView(ListView):
	model = Course
	template_name = 'courses/course_list.html'
	context_object_name = 'courses'
	paginate_by = 9
	def get_queryset( self ):
		# Ordonare dupa ID si numarare inscrieri
		qs = Course.objects.annotate(enrollment_count=Count('enrollment')).order_by('id')
		query = self.request.GET.get('q', '').strip()
		if query:
			qs = qs.filter(Q(title__icontains=query) | Q(description__icontains=query))
		return qs
	def get_context_data( self, **kwargs ):
		context = super().get_context_data(**kwargs)
		context['search_query'] = self.request.GET.get('q', '')
		context['news_list'] = News.objects.all().order_by('-created_at')
		return context
class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/course_detail.html'
	context_object_name = 'course'
	def get_context_data( self, **kwargs ):
		context = super().get_context_data(**kwargs)
		course = self.get_object()
		context['enrollment_count'] = Enrollment.objects.filter(course=course).count()
		if self.request.user.is_authenticated:
			# FIX: Folosim student in loc de user conform modelului tau
			context['is_enrolled'] = Enrollment.objects.filter(student=self.request.user, course=course).exists()
			context['is_instructor'] = (course.instructor == self.request.user)
		else:
			context['is_enrolled'] = False
			context['is_instructor'] = False
		return context
class CourseCreateView(LoginRequiredMixin, CreateView):
	model = Course
	form_class = CourseForm
	template_name = 'courses/course_form.html'
	success_url = reverse_lazy('course_list')
	def form_valid( self, form ):
		form.instance.instructor = self.request.user
		messages.success(self.request, f'Course "{form.instance.title}" created successfully!')
		return super().form_valid(form)
class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Course
	form_class = CourseForm
	template_name = 'courses/course_form.html'
	success_url = reverse_lazy('course_list')
	def test_func( self ):
		course = self.get_object()
		return self.request.user == course.instructor or self.request.user.is_superuser
class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Course
	template_name = 'courses/course_confirm_delete.html'
	success_url = reverse_lazy('course_list')
	def test_func( self ):
		course = self.get_object()
		return self.request.user == course.instructor or self.request.user.is_superuser
class EnrollmentCreateView(LoginRequiredMixin, CreateView):
	model = Enrollment
	fields = []
	success_url = reverse_lazy('course_list')
	def dispatch( self, request, *args, **kwargs ):
		self.course = get_object_or_404(Course, pk=kwargs['course_pk'])
		# FIX: Folosim student in loc de user
		if Enrollment.objects.filter(student=request.user, course=self.course).exists():
			messages.warning(request, 'You are already enrolled in this course.')
			return redirect('course_detail', pk=self.course.pk)
		return super().dispatch(request, *args, **kwargs)
	def form_valid( self, form ):
		form.instance.student = self.request.user
		form.instance.course = self.course
		response = super().form_valid(form)
		send_mail('Enrollment Confirmation', f'Hi {self.request.user.username}, you enrolled in "{self.course.title}".', 'noreply@mikrolearning.com', [self.request.user.email], fail_silently=True)
		messages.success(self.request, f'Enrolled in "{self.course.title}"! Confirmation email sent.')
		return response
class RegisterView(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	def form_valid( self, form ):
		messages.success(self.request, 'Account created! Please login.')
		return super().form_valid(form)
def home_index( request ):
	news_list = News.objects.all().order_by('-created_at')[:5]
	popular_courses = Course.objects.all().order_by('id')[:5]
	return render(request, 'home/index.html', { 'news_list': news_list, 'popular_courses': popular_courses })
class MyCoursesListView(LoginRequiredMixin, ListView):
	model = Enrollment
	template_name = 'courses/my_courses.html'
	context_object_name = 'enrollments'
	def get_queryset( self ):
		# FIX: Folosim student in loc de user
		return Enrollment.objects.filter(student=self.request.user).select_related('course').order_by('course__id')
@login_required
def enroll_in_course( request, pk ):
	course = get_object_or_404(Course, pk=pk)
	# FIX: Folosim student in loc de user
	enrollment, created = Enrollment.objects.get_or_create(student=request.user, course=course)
	if created:
		messages.success(request, f'You have successfully enrolled in {course.title}!')
	else:
		messages.info(request, f'You are already enrolled in {course.title}.')
	return redirect('course_detail', pk=pk)
