from weddingSite.models import *

class Gift(models.Model):
    image = models.ImageField(upload_to='gifts', null=False, blank=False)
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class GiftAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status',)
    list_display_links = ('id', 'name',)