from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CourseForm
from .models import Course, Enrollment


class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 9

    def get_queryset(self):
        qs = Course.objects.annotate(enrollment_count=Count('enrollment')).order_by('-created_at')
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        context['enrollment_count'] = Enrollment.objects.filter(course=course).count()
        if self.request.user.is_authenticated:
            context['is_enrolled'] = Enrollment.objects.filter(
                student=self.request.user, course=course
            ).exists()
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

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        messages.success(self.request, f'Cursul "{form.instance.title}" a fost creat cu succes!')
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

    def test_func(self):
        course = self.get_object()
        return self.request.user == course.instructor

    def form_valid(self, form):
        messages.success(self.request, f'Cursul "{form.instance.title}" a fost actualizat!')
        return super().form_valid(form)


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')

    def test_func(self):
        course = self.get_object()
        return self.request.user == course.instructor

    def form_valid(self, form):
        messages.success(self.request, 'Cursul a fost sters cu succes.')
        return super().form_valid(form)


class EnrollmentCreateView(LoginRequiredMixin, CreateView):
    model = Enrollment
    fields = []
    success_url = reverse_lazy('course_list')

    def dispatch(self, request, *args, **kwargs):
        self.course = get_object_or_404(Course, pk=kwargs['course_pk'])
        if Enrollment.objects.filter(student=request.user, course=self.course).exists():
            messages.warning(request, 'Esti deja inscris la acest curs.')
            return redirect('course_detail', pk=self.course.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.student = self.request.user
        form.instance.course = self.course
        response = super().form_valid(form)
        send_mail(
            'Confirmare Inscriere MikroLearning',
            f'Salut {self.request.user.username}, te-ai inscris cu succes la cursul "{self.course.title}".',
            'noreply@mikrolearning.ro',
            [self.request.user.email],
            fail_silently=True,
        )
        messages.success(self.request, f'Te-ai inscris cu succes la "{self.course.title}"! Un email de confirmare a fost trimis.')
        return response
