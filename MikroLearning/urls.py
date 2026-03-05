from django.contrib import admin
from django.urls import include, path

from home.views import index
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', index, name='home'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('courses/', include('courses.urls')),
	]
