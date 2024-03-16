import secrets
import hmac
import hashlib
from weddingSite.models import *

class Guest(models.Model):
    name = models.CharField(max_length=100)
    # mesa = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    token = models.CharField(max_length=100, null=False, blank=False)
    hmac_digest = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
@receiver(pre_save, sender=Guest)
def generate_guest_token_and_hmac(sender, instance, **kwargs):
    if not instance.token:
        instance.token = secrets.token_urlsafe(8)
        instance.hmac_digest = hmac.new(SECRET_KEY ,str(instance.token).encode('utf-8'), digestmod=hashlib.sha256).hexdigest()