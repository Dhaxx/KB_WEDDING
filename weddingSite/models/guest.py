from weddingSite.models import *

class TypeFilter(admin.SimpleListFilter):
    title = 'type'
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        return (
            (0, 'Convidado'),
            (1, 'Padrinho'),
        )

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(group__type=self.value())
        return queryset

class Guest(models.Model):
    name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, blank=True, null=True, related_name='guests')
    group = models.ForeignKey(GroupGuest, on_delete=models.SET_NULL, blank=True, null=True, related_name='members')

    def __str__(self):
        return self.name
    
@receiver(pre_save, sender=GroupGuest)
def generate_group_guest_token_and_hmac(sender, instance, **kwargs):
    if not instance.token:
        token = secrets.token_urlsafe(8)
        token = token.replace('I', 'i').replace('l', 'L').replace(' ', '_')
        instance.token = token
    key = bytes(SECRET_KEY, 'utf-8')
    instance.hmac_digest = hmac.new(key, str(instance.token).encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

@receiver(post_save, sender=Guest)
def create_group_guest_for_single_guest(sender, instance, created, **kwargs):
    if created and not instance.group:
        group_guest = GroupGuest.objects.create(name=f'Família {instance.name}')
        instance.group = group_guest
        instance.save()
        gift_cart = GiftCart.objects.create(guestGroup=group_guest)
        gift_cart.save()

class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'table', 'group', 'type')
    list_display_links = ('id', 'name', 'group',)
    list_filter = ('group', TypeFilter)  # Adiciona o filtro personalizado aqui

    def type(self, obj):
        type_description = {0: 'Convidado', 1: 'Padrinho'}
        # Retorna a descrição baseada no valor de 'type' do grupo, se existir
        return type_description.get(obj.group.type, None) if obj.group else None