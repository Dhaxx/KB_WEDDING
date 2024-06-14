from django.shortcuts import render, redirect
from django.contrib import messages
from axes.handlers.proxy import AxesProxyHandler
from axes.utils import reset
from weddingSite.forms import LoginForm
from weddingSite.models import GroupGuest  # Certifique-se de importar o modelo correto

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data.get('token')
            group_guest = GroupGuest.objects.filter(token=token).first()
            if group_guest:
                # Resetar tentativas falhadas em caso de sucesso
                reset(request)
                
                request.session['group_guest_id'] = group_guest.id
                if group_guest.status in [0, 2]:
                    request.session['show_modal'] = True
                else:
                    request.session['show_modal'] = False
                return redirect('home')  # substitua 'home' pelo nome da sua URL de destino
            else:
                # Registrar tentativa falhada
                credentials = {
                    'username': 'invalid_token',
                }
                AxesProxyHandler.user_login_failed(sender=None, request=request, credentials=credentials)
                messages.error(request, 'Token Inválido! Tente Novamente.')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})
