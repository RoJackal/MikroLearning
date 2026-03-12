from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CourseForm
from .models import Course, Enrollment
class CourseListView(ListView):
	model = Course
	template_name = 'courses/course_list.html'
	context_object_name = 'courses'
class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/course_detail.html'
class CourseCreateView(LoginRequiredMixin, CreateView):
	model = Course
	form_class = CourseForm
	template_name = 'courses/course_form.html'
	success_url = reverse_lazy('course_list')
	def form_valid( self, form ):
		form.instance.instructor = self.request.user
		return super().form_valid(form)
class CourseUpdateView(LoginRequiredMixin, UpdateView):
	model = Course
	form_class = CourseForm
	template_name = 'courses/course_form.html'
	success_url = reverse_lazy('course_list')
class CourseDeleteView(LoginRequiredMixin, DeleteView):
	model = Course
	template_name = 'courses/course_confirm_delete.html'
	success_url = reverse_lazy('course_list')
class EnrollmentCreateView(LoginRequiredMixin, CreateView):
	model = Enrollment
	fields = ['course']
	success_url = reverse_lazy('course_list')
	def form_valid( self, form ):
		form.instance.student = self.request.user
		response = super().form_valid(form)
		send_mail(
				'Confirmare Inscriere MikroLearning',
				f'Salut {self.request.user.username}, te-ai inscris cu succes la cursul {form.instance.course.title}.',
				'noreply@mikrolearning.ro',
				[self.request.user.email],
				fail_silently=True,
				)
		return response
