from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Client

def client_list(request):
    """
    Display the clients list.
    """
    # get a queryset of all the clients
    clients_qs = Client.objects.all()

    # paginate the clients list
    paginator = Paginator(clients_qs, 12) # display 8 clients per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'clients':page_obj}
    return render(request, 'client/client_list.html', context)

    

