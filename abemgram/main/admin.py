from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Customer

# Register your models here.
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete: False
    verbose_name_plural = 'customer'

class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)