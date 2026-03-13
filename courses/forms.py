from django import forms

from .models import Course
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
		if start and end and end < start:
			raise forms.ValidationError("End date cannot be earlier than start date.")
		return cleaned_data
