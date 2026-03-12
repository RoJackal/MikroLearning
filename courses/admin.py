from django.contrib import admin

from .models import Course, Enrollment
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'instructor', 'price', 'start_date', 'end_date')
	search_fields = ('title', 'description')
	list_filter = ('instructor', 'start_date')
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
	list_display = ('student', 'course', 'date_enrolled')
	list_filter = ('course', 'date_enrolled')
	search_fields = ('student__username', 'course__title')
