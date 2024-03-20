from django.urls import path
from weddingSite.views.HomeView import home_view

urlpatterns = [
    path('', home_view, name='home'),
]