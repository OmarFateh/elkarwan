from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from .models import Company, Category, Product
from product.custom_admin.forms import ProductAdminForm
from product.custom_admin.filters import ProductFilter

class DontLog:
    def log_addition(self, *args):
        return ''

    def log_change(self, *args):
        return ''

    def log_deletion(self, *args):
        return ''       

class CategoryInline(admin.TabularInline):
    """
    """
    model  = Category
    fields = ['name', 'company', 'icon_type']
    extra = 1

class CompanyAdmin(DontLog, admin.ModelAdmin):
    """
    """
    date_hierarchy = 'timestamp'
    list_display   = ['name', 'timestamp'] 
    list_filter    = ['timestamp']
    search_fields  = ['name',]
    fields         = ['name', 'image']
    inlines        = [CategoryInline] 
    ordering       = ['-timestamp']

    class Media:
        js = ('js/admin_company.js',)

class ProductAdmin(DontLog, admin.ModelAdmin):
    """
    """
    form           = ProductAdminForm
    date_hierarchy = 'timestamp'
    list_display   = ['name', 'company', 'category', 'model', 'code', 'timestamp'] 
    list_filter    = [('company', ProductFilter), 'timestamp']
    search_fields  = ['name', 'model', 'code']
    ordering       = ['-timestamp']

    class Media:
        js = ('js/admin_main.js',)

admin.site.index_title = 'My administration'
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)