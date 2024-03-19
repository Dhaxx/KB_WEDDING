from django.urls import path
from weddingSite.views.LoginView import login_view

urlpatterns = [
    path('', login_view, name='login'),
]
