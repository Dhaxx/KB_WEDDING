from weddingSite.models import *

class GiftCart(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True, related_name='gift_cart')
    gift = models.ForeignKey(Gift, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.guest.name if self.guest else 'None'
    
class GiftCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'guest', 'total',)
    list_display_links = ('id', 'guest',)