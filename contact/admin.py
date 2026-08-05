from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'category', 'show',
    ordering = '-id',

    search_fields = 'id' ,'first_name', 
    list_display_links = 'id',
    list_editable = 'first_name', 'last_name', 'phone', 'category', 'show',

@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = 'id', 'name', 
    list_display_links = 'name',
    ordering = '-id',