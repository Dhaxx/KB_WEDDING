from django.http import HttpResponse
from django.shortcuts import render, redirect
from weddingSite.models import GroupGuest

def home_view(request):
    if 'group_guest_id' not in request.session:
        return redirect('login')
    return render(request, 'home/home.html')

def confirm_presence(request):
    print(request.POST)  # Imprime o POST da requisição
    if 'group_guest_id' in request.session and 'is_attending' in request.POST:
        group_guest_id = request.session['group_guest_id']
        is_attending = request.POST['is_attending'] == 'true'
        group_guest = GroupGuest.objects.get(id=group_guest_id)
        group_guest.update_presence(is_attending)
    return HttpResponse(status=200)