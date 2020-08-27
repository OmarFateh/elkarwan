from django.shortcuts import render


def home(request):
    """
    Take a request, and render the home page.
    """
    return render(request, 'home/home.html', {})


def custom_page_not_found_view(request, exception):
    """
    custom 404 error page
    """
    return render(request, '404.html')