from django.shortcuts import render, redirect
from django.contrib import messages
from weddingSite.models import *

from .HomeView import home_view
from .LoginView import login_view