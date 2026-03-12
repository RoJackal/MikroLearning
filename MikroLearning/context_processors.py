from courses.models import Course
def popular_courses( request ):
	# Returns the 3 most recently added courses
	courses = Course.objects.all().order_by('-created_at')[:3]
	return { 'popular_courses': courses }
