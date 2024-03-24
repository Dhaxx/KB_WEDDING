from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from main.settings.development import SECRET_KEY
from django.contrib import admin
import secrets
import hmac
import hashlib

STATUS_CHOICES = (
    (0, 'PENDENTE'),
    (1, 'EU IREI'),
    (2, 'NÃO IREI'),
)

from .table import Table, TableAdmin
from .gift import Gift, GiftAdmin
from .guestGroup import GroupGuest
from .giftCart import GiftCart, GiftCartAdmin
from .guest import Guest, GuestAdmin