from django import forms 

class LoginForm(forms.Form):
	name = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	name = forms.CharField(max_length=30)
	e_mail = forms.EmailField()
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)

class CommentForm(forms.Form):
	comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}), max_length=30)