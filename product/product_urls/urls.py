from django.urls import path

from ..views import product_list

urlpatterns = [

    # products/{company_id}/{company_slug}/{category_id}/{category_slug}
    path('<str:category_slug>/', product_list, name='product-list'),

]