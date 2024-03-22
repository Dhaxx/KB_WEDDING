from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def home_view(request):
    if 'guest_id' not in request.session:
        return redirect('login')
    return render(request, 'home/home.html',)