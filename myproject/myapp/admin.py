from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from myapp.models import *
from myapp.models import Post

class postAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title']
    ordering = ['id']

admin.site.register(Post,postAdmin)

admin.site.register(Mobels)
