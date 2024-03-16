from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from main.settings.development import SECRET_KEY

STATUS_CHOICES = (
    (0, 'PENDENTE'),
    (1, 'EU IREI'),
    (2, 'NÃO IREI'),
)

from .guest import Guest