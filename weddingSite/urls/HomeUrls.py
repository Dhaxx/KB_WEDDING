from django.urls import path
from weddingSite.views.HomeView import home_view, confirm_presence

urlpatterns = [
    path('', home_view, name='home'),
    path('confirm_presence/', confirm_presence, name='confirm_presence'),
]