from django import forms

from .models import Course
class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['title', 'description', 'start_date', 'end_date', 'price', 'materials']
		widgets = {
			'start_date': forms.DateInput(attrs={ 'type': 'date', 'class': 'w-full p-2 border rounded bg-slate-50 dark:bg-slate-700' }),
			'end_date':   forms.DateInput(attrs={ 'type': 'date', 'class': 'w-full p-2 border rounded bg-slate-50 dark:bg-slate-700' }),
			}
	
	def clean( self ):
		cleaned_data = super().clean()
		start = cleaned_data.get("start_date")
		end = cleaned_data.get("end_date")
		if start and end and end < start:
			raise forms.ValidationError("Eroare: Data de final este inaintea datei de inceput.")
		return cleaned_data
