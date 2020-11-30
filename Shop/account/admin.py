from django.contrib import admin
from .models import Profile

# admin.site.register(Profile)


@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    list_filter = ('address', 'user', 'order')

# admin.site.register(Profile, AuthorAdmin)
