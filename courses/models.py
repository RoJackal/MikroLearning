from django.contrib.auth.models import User
from django.db import models
class Course(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	instructor = models.ForeignKey(User, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	materials = models.FileField(upload_to='courses/', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__( self ):
		return f"Course: {self.title} - Instructor: {self.instructor.username}"
class Enrollment(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	date_enrolled = models.DateTimeField(auto_now_add=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__( self ):
		return f"Enrollment: {self.student.username} - {self.course.title}"
