from django.urls import path
from weddingSite.views.HomeView import home_view, confirm_presence, add_gift

urlpatterns = [
    path('', home_view, name='home'),
    path('confirm_presence/', confirm_presence, name='confirm_presence'),
    path('add_to_gift_cart/<int:gift_id>/', add_gift, name='add_to_gift_cart'),
]