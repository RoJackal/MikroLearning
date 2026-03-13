from django.contrib import admin
from django.urls import include, path

from courses.views import CourseListView, home_index
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', home_index, name='home'),
	path('courses/', CourseListView.as_view(), name='course_list'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('portal/', include('courses.urls')),
	]
