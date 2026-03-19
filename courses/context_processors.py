from django.db.models import Count

from .models import Course
def popular_courses( request ):
	try:
		# Requirement: Return popular courses (User requested top 5)
		courses = Course.objects.annotate(enrollment_count=Count('enrollment')).order_by('-enrollment_count')[:5]
		return { 'popular_courses': courses }
	except Exception:
		return { 'popular_courses': [] }
