from django.urls import path

from . import views
from .views import (CourseCreateView, CourseDeleteView, CourseDetailView, CourseListView, CourseUpdateView, MyCoursesListView, RegisterView)
urlpatterns = [
	# Afisarea tuturor certificarilor disponibile
	path('', CourseListView.as_view(), name='course_list'),
	# Vizualizarea detaliilor complete pentru o certificare
	path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
	# Formular pentru adaugarea unei noi certificari
	path('course/add/', CourseCreateView.as_view(), name='course_add'),
	# Modificarea datelor unei certificari existente pe baza PK
	path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
	# Eliminarea definitiva a unei certificari din baza de date
	path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
	# Procesarea inscrierii unui student la o certificare
	path('course/<int:pk>/enroll/', views.enroll_in_course, name='course_enroll'),
	# Listarea certificarilor la care utilizatorul curent este inscris
	path('my-courses/', MyCoursesListView.as_view(), name='my_courses'),
	# Formular de creare cont nou pentru studenti
	path('register/', RegisterView.as_view(), name='register'),
	]
