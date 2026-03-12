from django.urls import path

from .views import (CourseCreateView, CourseDeleteView, CourseDetailView, CourseListView, CourseUpdateView, EnrollmentCreateView)
urlpatterns = [
	path('', CourseListView.as_view(), name='course_list'),
	path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
	path('course/add/', CourseCreateView.as_view(), name='course_add'),
	path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
	path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
	path('course/enroll/', EnrollmentCreateView.as_view(), name='course_enroll'),
	]
