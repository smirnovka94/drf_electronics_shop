from django.contrib import admin

from users.models import User
@admin.register(User)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'is_active', 'is_superuser')
