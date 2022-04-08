from django import forms

class MyUserForm(forms.Form):
    name = forms.CharField(label = 'Your name', max_length = 20)
    email = forms.CharField(label = 'Your email', max_length = 20)
    password = forms.CharField(label = 'Your password', max_length = 20)
    DNI = forms.CharField(label = 'Your DNI', max_length = 9)

