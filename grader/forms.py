from django import forms

class ProblemForm(forms.Form):
	user_file = forms.FileField(label='Select file')