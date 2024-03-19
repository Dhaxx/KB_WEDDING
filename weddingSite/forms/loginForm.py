from weddingSite.forms import *

class LoginForm(forms.Form):
    token = forms.CharField()