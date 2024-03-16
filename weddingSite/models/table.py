from weddingSite.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Table(models.Model):
    name = models.CharField(max_length=100)
    fk_guests = models.ManyToManyField('Guest', related_name='guest_tables')

    def __str__(self):
        return self.name

    def clean(self):
        if self.fk_guests.count() > 6:
            raise ValidationError(_("A mesa não pode ter mais de 6 convidados."))
        
class GuestInline(admin.TabularInline):
    model = Table.fk_guests.through

class TableAdmin(admin.ModelAdmin):
    def num_guests(self, obj):
        return obj.fk_guests.count()
    num_guests.short_description = 'Número de Convidados'

    inlines = [GuestInline]

    list_display = ('id', 'name')
    exclude = 'fk_guests',