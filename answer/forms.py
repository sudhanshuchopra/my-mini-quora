from django import forms
from .models import answer
class postansform(forms.ModelForm):
	class Meta:
		model=answer
		fields=['body']