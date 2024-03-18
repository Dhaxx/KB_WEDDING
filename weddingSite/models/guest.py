import secrets
import hmac
import hashlib
from weddingSite.models import *

class Guest(models.Model):
    name = models.CharField(max_length=100)
    fk_table = models.ForeignKey('Table', on_delete=models.SET_NULL, blank=True, null=True, related_name='guests')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    token = models.CharField(max_length=100, null=True, blank=True)
    hmac_digest = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name
    
@receiver(pre_save, sender=Guest)
def generate_guest_token_and_hmac(sender, instance, **kwargs):
    if not instance.token:
        instance.token = secrets.token_urlsafe(8)
    if not instance.hmac_digest:
        key = bytes(SECRET_KEY, 'utf-8')
        instance.hmac_digest = hmac.new(key ,str(instance.token).encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

@receiver(post_save, sender=Guest)
def created_gift_cart(sender, instance, created, **kwargs):
    if created:
        gift_cart = GiftCart.objects.create(owner=instance, total=0)
        instance.gift_cart = gift_cart
        instance.save()    

class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'fk_table', 'token',)
    exclude = ('hmac_digest','token',)