from django.contrib import admin
from accounts.models import User
from django.contrib.auth.models import Permission

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Permission)
class Permissinon(admin.ModelAdmin):
    pass