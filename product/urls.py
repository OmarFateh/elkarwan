from django.urls import path, include

from . import views

urlpatterns = [

    # companies/
    path('', views.company_list, name='company-list'),

    # companies/{company_slug}
    path('<str:slug>/', views.category_list, name='category-list'), 
    
    # companies/{company_slug}/{category_slug}
    path('<str:comapny_slug>/', include('product.product_urls.urls')),
       


]