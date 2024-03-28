from django.http import HttpResponse
from django.shortcuts import render, redirect
from weddingSite.models import GroupGuest, Gift

def home_view(request):
    if 'group_guest_id' not in request.session:
        return redirect('login')
    group_guest_id = request.session['group_guest_id']
    group_guest = GroupGuest.objects.get(id=group_guest_id)
    
    gifts = Gift.objects.filter(status=False)

    gift_cart = group_guest.gift_cart.get()

    show_modal = request.session.get('show_modal', False) and group_guest.status in [0, 2] 

    return render(request, 'home/home.html', {'gifts': gifts, 'gift_cart': gift_cart, 'show_modal': show_modal, 'group_guest': group_guest})  
def confirm_presence(request):
    if 'group_guest_id' in request.session and 'is_attending' in request.POST:
        group_guest_id = request.session['group_guest_id']
        is_attending = request.POST['is_attending'] == 'true'
        group_guest = GroupGuest.objects.get(id=group_guest_id)
        group_guest.update_presence(is_attending)
        if is_attending:
            request.session['show_modal'] = False  
    return HttpResponse(status=200)