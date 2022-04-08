from django import forms

class MyUserForm(forms.Form):
    name = forms.CharField(label = 'Your name', max_length = 20)
    mail = forms.CharField(label = 'Your email', max_length = 20)
    password = forms.CharField(label = 'Your password', max_length = 20)
