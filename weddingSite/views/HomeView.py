from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from weddingSite.models import GroupGuest, Gift, GiftCart

def home_view(request):
    if 'group_guest_id' not in request.session:
        return redirect('login')
    group_guest_id = request.session['group_guest_id']
    group_guest = GroupGuest.objects.get(id=group_guest_id)

    gift_cart = GiftCart.objects.filter(guestGroup=group_guest).first()
    
    gift_choosed = gift_cart.gift
    gifts = Gift.objects.filter(status=False)

    show_modal = request.session.get('show_modal', False) and group_guest.status in [0, 2] 

    return render(request, 'home/home.html', {'gifts': gifts, 'gift_choosed': gift_choosed, 'show_modal': show_modal, 'group_guest': group_guest})  

def confirm_presence(request):
    if 'group_guest_id' in request.session and 'is_attending' in request.POST:
        group_guest_id = request.session['group_guest_id']
        is_attending = request.POST['is_attending'] == 'true'
        group_guest = GroupGuest.objects.get(id=group_guest_id)
        group_guest.update_presence(is_attending)
        if is_attending:
            request.session['show_modal'] = False  
    return HttpResponse(status=200)

@login_required
def add_gift(request):
    if 'group_guest_id' not in request.session:
        return redirect('login')
    
    gift = get_object_or_404(Gift, id=request.POST['gift_id'])
    group_guest_id = request.session['group_guest_id']
    group_guest = GroupGuest.objects.get(id=group_guest_id)

    GiftCart.objects.create(guestGroup=group_guest, gift=gift)

    return redirect('home')