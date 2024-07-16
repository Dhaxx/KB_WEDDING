from weddingSite.models import *

class GiftCart(models.Model):
    guestGroup = models.ForeignKey(GroupGuest, on_delete=models.CASCADE, null=True, related_name='gift_cart')
    gift = models.ForeignKey(Gift, on_delete=models.SET_NULL, null=True, blank=True, related_name='gift_cart')

    def __str__(self):
        return self.guestGroup.name if self.guestGroup else 'None'

class GiftCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'guestGroup', 'gift',)
    list_display_links = ('id', 'guestGroup', 'gift',)