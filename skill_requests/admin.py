from django.contrib import admin
from .models import SkillRequest, Message

@admin.register(SkillRequest)
class SkillRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'skill', 'status', 'created_at')
    list_filter = ('status', 'created_at')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('request', 'sender', 'timestamp')
