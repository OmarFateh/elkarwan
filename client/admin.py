from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    """
    Client admin model.
    """
    date_hierarchy = 'timestamp'
    list_display   = ['name', 'timestamp'] 
    list_filter    = ['timestamp']
    search_fields  = ['name']
    ordering       = ['-timestamp']

admin.site.register(Client, ClientAdmin)