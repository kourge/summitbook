from django.contrib import admin
from apps.people.models import Person
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class PersonInline(admin.StackedInline):
    model = Person
    fk_name = 'user'
    max_num = 1

class CustomUserAdmin(UserAdmin):
    inlines = [PersonInline, ]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

