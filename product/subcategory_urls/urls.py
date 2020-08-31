from django.urls import path, include

from ..views import subcategory_list

urlpatterns = [

    # companies/{company_slug}/{category_slug}/
    path('<str:category_slug>/', subcategory_list, name='subcategory-list'),

    # companies/{company_slug}/{category_slug}/{subcategory_slug}/
    path('<str:category_slug>/', include('product.product_urls.urls')),
]