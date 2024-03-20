from weddingSite.views import *
from weddingSite.forms import LoginForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data.get('token')
            guest = Guest.objects.filter(token=token).first()
            if guest:
                request.session['guest_id'] = guest.id
                return redirect('home')
            else:
                messages.error(request, 'Token Inválido')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})