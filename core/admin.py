from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp')
    readonly_fields = ('timestamp',)
    search_fields = ('name', 'email', 'subject', 'message')
