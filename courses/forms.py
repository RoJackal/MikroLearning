from django import forms

from .models import Course, Enrollment
class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['title', 'description', 'start_date', 'end_date', 'price', 'materials']
		widgets = {
			'title':       forms.TextInput(attrs={ 'class': 'w-full p-2 border rounded bg-slate-50 dark:bg-slate-700' }),
			'description': forms.Textarea(attrs={ 'class': 'w-full p-2 border rounded bg-slate-50 dark:bg-slate-700', 'rows': 4 }),
			'start_date':  forms.DateInput(attrs={ 'type': 'date', 'class': 'w-full p-2 border rounded bg-slate-50 dark:bg-slate-700' }),
			'end_date':    forms.DateInput(attrs={ 'type': 'date', 'class': 'w-full p-2 border rounded bg-slate-50 dark:bg-slate-700' }),
			'price':       forms.NumberInput(attrs={ 'class': 'w-full p-2 border rounded bg-slate-50 dark:bg-slate-700' }),
			'materials':   forms.ClearableFileInput(attrs={ 'class': 'w-full p-2 text-sm' }),
			}
	
	def clean( self ):
		cleaned_data = super().clean()
		start = cleaned_data.get("start_date")
		end = cleaned_data.get("end_date")
		price = cleaned_data.get("price")
		if start and end and end < start:
			raise forms.ValidationError("End date cannot be earlier than start date.")
		if price is not None and price < 0:
			raise forms.ValidationError("The price must be a positive value.")
		return cleaned_data
class EnrollmentForm(forms.ModelForm):
	class Meta:
		model = Enrollment
		fields = []
	
	def __init__( self, *args, **kwargs ):
		self.student = kwargs.pop('student', None)
		self.course = kwargs.pop('course', None)
		super().__init__(*args, **kwargs)
	def clean( self ):
		cleaned_data = super().clean()
		if Enrollment.objects.filter(student=self.student, course=self.course).exists():
			raise forms.ValidationError("You are already enrolled in this course.")
		return cleaned_data
