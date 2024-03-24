from weddingSite.models import *

class Guest(models.Model):
    name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, blank=True, null=True, related_name='guests')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    group = models.ForeignKey(GroupGuest, on_delete=models.SET_NULL, blank=True, null=True, related_name='members')

    def __str__(self):
        return self.name
    
@receiver(pre_save, sender=GroupGuest)
def generate_group_guest_token_and_hmac(sender, instance, **kwargs):
    if not instance.token:
        instance.token = secrets.token_urlsafe(8)
    key = bytes(SECRET_KEY, 'utf-8')
    instance.hmac_digest = hmac.new(key ,str(instance.token).encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

@receiver(post_save, sender=Guest)
def create_group_guest_for_single_guest(sender, instance, created, **kwargs):
    if created and not instance.group:
        group_guest = GroupGuest.objects.create(name=f'Família {instance.name}')
        instance.group = group_guest
        instance.save()
        gift_cart = GiftCart.objects.create(guestGroup=group_guest)
        gift_cart.save()

class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'table', 'group',)
    list_display_links = ('id', 'name',)