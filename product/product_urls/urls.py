from django.urls import path

from ..views import product_list

urlpatterns = [

    # companies/{company_slug}/{category_slug}/{subcategory_slug}/
    path('<str:subcategory_slug>/', product_list, name='product-list'),

]