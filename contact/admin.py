from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'phone', 'category',
    ordering = '-id',

    search_fields = 'id' ,'first_name', 
    list_display_links = 'id', 'first_name',

@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = 'id', 'name', 
    list_display_links = 'name',
    ordering = '-id',