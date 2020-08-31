"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from product.custom_admin.views import get_category, get_subcategory

# custom 404 error page
handler404 = 'home.views.custom_page_not_found_view'

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    # home
    path('', include(('home.urls', 'home'), namespace='home')),

    # about
    path('about/', include(('about.urls', 'about'), namespace='about')),

    # product
    path('companies/', include(('product.urls', 'product'), namespace='product')),

    # product category dropdown
    path('getCategory/', get_category, name='category'), 

    # product subcategory dropdown
    path('getSubcategory/', get_subcategory, name='subcategory'),

    # client
    path('clients/', include(('client.urls', 'client'), namespace='client')),

    # contact
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
