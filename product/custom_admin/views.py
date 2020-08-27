import json
from django.http import HttpResponse

from product.models import Category

def get_category(request): 
    """
    Take request and return json data of a list of filtered categories according to the selected company. 
    """
    company_id = request.GET.get('id', '') 
    category_lst = list(Category.objects.filter(company_id=int(company_id)).values('id', 'name')) 
    return HttpResponse(json.dumps(category_lst), content_type="application/json") 



