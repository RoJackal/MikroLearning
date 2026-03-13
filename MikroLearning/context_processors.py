from courses.models import Course
def popular_courses( request ):
	try:
		# Fetches the top 5 courses sorted by ID to match your previous request
		courses = Course.objects.all().order_by('id')[:5]
		return { 'popular_courses': courses }
	except Exception:
		return { 'popular_courses': [] }
