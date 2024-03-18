from weddingSite.models import *

class GiftCart(models.Model):
    fk_guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    fk_gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    total = models.FloatField()

    def __str__(self):
        return self.fk_guest.name + " - " + self.fk_gift.name
    
class GiftCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_guest', 'total',)