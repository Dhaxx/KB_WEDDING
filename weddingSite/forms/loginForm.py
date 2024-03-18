from weddingSite import forms

class LoginForm(forms.Form):
    token = forms.CharField()