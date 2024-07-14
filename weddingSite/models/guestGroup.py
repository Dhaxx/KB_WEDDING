from weddingSite.models import *

class GroupGuest(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=100, unique=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    type = models.IntegerField(choices=GROUP_TYPE, default=0)

    def update_presence(self, is_attending):
        self.status = 1 if is_attending else 2
        self.save()

    def __str__(self):
        return f"{self.name}"
    
class GroupGuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'token', 'type')
    list_display_links = ('name',)