from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import UserCreationForm, UserChangeForm
from users.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','phone','password','is_active','is_superuser','is_staff')
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('phone','email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ( )}),
        ('Groups', {'fields': ()}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('phone','email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ( )}),
        ('Groups', {'fields': ()}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    search_fields = ('email', 'name', 'phone')

    ordering =()
    filter_horizontal = ()

admin.site.register(User,UserAdmin)