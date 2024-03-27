from weddingSite.views import *
from weddingSite.forms import LoginForm

def login_view(request):
    show_modal = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data.get('token')
            group_guest = GroupGuest.objects.filter(token=token).first()
            if group_guest:
                request.session['group_guest_id'] = group_guest.id
                if group_guest.status in [0, 2]:
                    show_modal = True
                return render(request, 'home/home.html', {'show_modal': show_modal, 'group_guest': group_guest})
            else:
                messages.error(request, 'Token Inválido! Tente Novamente.')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})