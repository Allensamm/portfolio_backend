# app_name/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser, Post



admin.site.register(AppUser)
admin.site.register(Post)
