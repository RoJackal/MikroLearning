from django.urls import path

from .views import CourseListView, SignUpView
urlpatterns = [
	path('', CourseListView.as_view(), name='course-list'),
	path('signup/', SignUpView.as_view(), name='signup'),
	]
