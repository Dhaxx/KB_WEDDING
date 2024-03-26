from django.contrib import admin
from .models import *

admin.site.register(Table, TableAdmin)
admin.site.register(GroupGuest, GroupGuestAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Gift, GiftAdmin)
admin.site.register(GiftCart, GiftCartAdmin)