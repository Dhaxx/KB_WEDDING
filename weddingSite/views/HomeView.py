from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import redirect

def home_view(request):
    if 'guest_id' not in request.session:
        return redirect('login')
    return HttpResponse('<h1>Home</h1>')