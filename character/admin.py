# main/admin.py
from django.contrib import admin
from .models import (
    CharacterClass,
    Specialization, Race, Character
)


@admin.register(CharacterClass)
class CharacterClassAdmin(admin.ModelAdmin):
    list_display = ('get_name_display', 'specs_count')
    readonly_fields = ('name',)
    
    def specs_count(self, obj):
        return obj.specializations.count()
    specs_count.short_description = 'Специализаций'


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'character_class', 'get_role_display')
    list_filter = ('character_class', 'role')
    readonly_fields = ('character_class', 'name', 'role')


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('get_name_display', 'get_faction_display')
    list_filter = ('faction',)
    readonly_fields = ('name', 'faction')


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'user', 'get_class', 'specialization',
        'race', 'item_level', 'is_main'
        )
    list_filter = ('faction', 'character_class', 'race')
    search_fields = ('name', 'user__username')
    list_editable = ('is_main', 'item_level')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Основное', {
            'fields': ('name', 'user', 'is_main')
        }),
        ('Характеристики', {
            'fields': ('character_class', 'specialization', 'race', 'faction')
        }),
        ('Геймплей', {
            'fields': ('item_level',)
        }),
    )

    def save_model(self, request, obj, form, change):
        """Сохраняем с проверкой."""
        obj.clean()
        super().save_model(request, obj, form, change)
    
    def get_class(self, obj):
        return obj.character_class.get_name_display()
    get_class.short_description = 'Класс'
