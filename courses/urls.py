from django.urls import path

from .views import (CourseCreateView, CourseDeleteView, CourseDetailView, CourseListView, CourseUpdateView, EnrollmentCreateView, RegisterView)
urlpatterns = [
	path('', CourseListView.as_view(), name='course_list'),
	path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
	path('course/add/', CourseCreateView.as_view(), name='course_add'),
	path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
	path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
	path('course/<int:course_pk>/enroll/', EnrollmentCreateView.as_view(), name='course_enroll'),
	path('register/', RegisterView.as_view(), name='register'),
	]
