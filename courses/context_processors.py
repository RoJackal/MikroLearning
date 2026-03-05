from django.db.models import Count

from .models import Course
def popular_courses( request ):
	try:
		# Uses 'enrollment' because it is the default related name for the Enrollment model
		courses = Course.objects.annotate(enrollment_count=Count('enrollment')).order_by('-enrollment_count')[:5]
		return { 'popular_courses': courses }
	except Exception:
		return { 'popular_courses': [] }
