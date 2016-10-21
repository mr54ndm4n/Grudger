from django import forms

class Profile_PicForm(forms.Form):
	profile_pic = forms.FileField(label='Select file')

class ProblemForm(forms.Form):
	user_file = forms.FileField(label='Select file')