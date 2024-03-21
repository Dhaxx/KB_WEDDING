from django.http import HttpResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return HttpResponse('<h1>Home</h1>')