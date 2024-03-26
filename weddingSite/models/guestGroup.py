from weddingSite.models import *

class GroupGuest(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=100, unique=True)
    hmac_digest = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"
    
class GroupGuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'token',)
    list_display_links = ('name',)