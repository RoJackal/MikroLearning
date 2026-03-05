from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Course
class CourseListView(ListView):
	model = Course
	template_name = 'courses/course_list.html'
	context_object_name = 'courses'
class SignUpView(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'
