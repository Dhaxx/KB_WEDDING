from weddingSite.views import *
from weddingSite.forms import LoginForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data.get('token')
            group_guest = GroupGuest.objects.filter(token=token).first()
            if group_guest:
                guest = group_guest.members.first()
                if guest:
                    request.session['guest_id'] = guest.id
                    return redirect('home')
                else:
                    messages.error(request, 'Grupo sem convidados! Tente Novamente.')
            else:
                messages.error(request, 'Token Inválido! Tente Novamente.')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})