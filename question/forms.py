from django import forms
from .models import Question
class addform(forms.ModelForm):
	class Meta:
		model=Question
		fields=['title','body']