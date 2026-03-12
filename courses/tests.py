from django.urls import path

from . import views
app_name = 'courses'

urlpatterns = [
	# List all courses
	path('', views.CourseListView.as_view(), name='list'),
	# Course detail
	path('<slug:title>/', views.CourseDetailView.as_view(), name='detail'),
	# CRUD (instructor only)
	path('create/', views.CourseCreateView.as_view(), name='create'),
	path('<slug:title>/update/', views.CourseUpdateView.as_view(), name='update'),
	path('<slug:title>/delete/', views.CourseDeleteView.as_view(), name='delete'),
	# Enrollment (student)
	path('<slug:title>/enroll/', views.EnrollmentCreateView.as_view(), name='enroll'),
	]
