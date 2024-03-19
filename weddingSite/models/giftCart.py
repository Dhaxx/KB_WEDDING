from weddingSite.models import *

class GiftCart(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True, related_name='gift_cart')
    gifts = models.ManyToManyField('Gift', related_name='gift_cart')

    def __str__(self):
        return self.guest.name if self.guest else 'None'
    
    def total(self):
        return sum([gift.price for gift in self.gifts.all()])

class GiftCartInline(admin.TabularInline):
    model = GiftCart.gifts.through
    
class GiftCartAdmin(admin.ModelAdmin):
    def total(self, obj):
        return obj.total()
    total.short_description = 'Total'

    inlines = [GiftCartInline] if GiftCart.gifts.through not in admin.site._registry else []

    list_display = ('id', 'guest', 'total',)
    list_display_links = ('id', 'guest',)
    exclude = 'gifts',