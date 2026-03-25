from django.contrib import admin
from .models import Category, Skill

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
