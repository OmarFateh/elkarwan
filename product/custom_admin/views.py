import json
from django.shortcuts import render
from django.http import HttpResponse

from product.models import Category, Subcategory

def get_category(request): 
    """
    Take request and return json data of a list of filtered categories according to the selected company. 
    """
    print("hey")
    company_id = request.GET.get('id', '') 
    print(company_id)
    category_lst = list(Category.objects.filter(company_id=int(company_id)).values('id', 'name')) 
    return HttpResponse(json.dumps(category_lst), content_type="application/json") 


def get_subcategory(request):
    """
    Take request and return json data of a list of filtered subcategories according to the selected category. 
    """
    print("hey1")
    category_id = request.GET.get('id', '') 
    print(category_id)
    subcategory_lst = list(Subcategory.objects.filter(category_id=int(category_id)).values('id', 'name')) 
    return HttpResponse(json.dumps(subcategory_lst), content_type="application/json") 

