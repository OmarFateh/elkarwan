from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Company, Category, Subcategory, Product

def company_list(request):
    """
    Display the companies list.
    """
    # get a queryset of all the companies
    companies = Company.objects.all()

    categories, subcategories, products = None, None, None
    page_obj_category, page_obj_subcategory, page_obj_product = None, None, None
    page_number = request.GET.get('page')
    # Search by company name, category, subcategory, product name, model, or code.
    query = request.GET.get('q')
    if query:
        companies = Company.objects.filter(name__icontains=query) 
        categories = Category.objects.filter(name__icontains=query)
        subcategories = Subcategory.objects.filter(name__icontains=query)
        products = Product.objects.filter(
            Q(name__icontains=query)|
            Q(model__icontains=query)|
            Q(code__icontains=query)
        ).distinct() 

    # paginate the companies list
    paginator_company = Paginator(companies, 12) # display 8 companies per page.
    page_obj_company = paginator_company.get_page(page_number)
    
    if categories:
        # paginate the resulted categories list
        paginator_category = Paginator(categories, 12) # display 8 categories per page.
        page_obj_category = paginator_category.get_page(page_number)

    if subcategories:
        # paginate the subcategories list
        paginator_subcategory = Paginator(subcategories, 12) # display 8 subcategories per page.
        page_obj_subcategory = paginator_subcategory.get_page(page_number)

    if products:
        # paginate the resulted products list
        paginator_product = Paginator(products, 12) # display 4 products per page.
        page_obj_product = paginator_product.get_page(page_number)

    context = {'query':query, 
                'companies':page_obj_company, 
                'categories':page_obj_category, 
                'subcategories':page_obj_subcategory,
                'products':page_obj_product, 
            }
    return render(request, 'product/company_list.html', context)


def category_list(request, slug=None):
    """
    Display the company categories list.
    """
    # get the current company
    company = get_object_or_404(Company, slug=slug) 

    # get a queryset of all the categories of the current company
    categories = company.categories.all()

    companies, subcategories, products = None, None, None
    page_obj_company, page_obj_subcategory, page_obj_product = None, None, None
    page_number = request.GET.get('page')

    # Search by company name, category, subcategory, product name, model, or code.
    query = request.GET.get('q')
    if query:
        companies = Company.objects.filter(name__icontains=query) 
        categories = Category.objects.filter(name__icontains=query)
        subcategories = Subcategory.objects.filter(name__icontains=query)
        products = Product.objects.filter(
            Q(name__icontains=query)|
            Q(model__icontains=query)|
            Q(code__icontains=query)
        ).distinct() 

    # paginate the categories list
    paginator_category = Paginator(categories, 12) # display 8 categories per page.
    page_obj_category = paginator_category.get_page(page_number)

    if companies:
        # paginate the companies list
        paginator_company = Paginator(companies, 12) # display 8 companies per page.
        page_obj_company = paginator_company.get_page(page_number)
    
    if subcategories:
        # paginate the subcategories list
        paginator_subcategory = Paginator(subcategories, 12) # display 8 subcategories per page.
        page_obj_subcategory = paginator_subcategory.get_page(page_number)

    if products:
        # paginate the resulted products list
        paginator_product = Paginator(products, 12) # display 4 products per page.
        page_obj_product = paginator_product.get_page(page_number)

    context = { 'query':query,
                'categories':page_obj_category, 
                'company':company, 
                'companies':page_obj_company,
                'subcategories':page_obj_subcategory,
                'products':page_obj_product,
            }
    return render(request, 'product/category_list.html', context)


def subcategory_list(request, comapny_slug=None, category_slug=None):
    """
    Display the company category subcategories list.
    """
    # get the current category
    category = get_object_or_404(Category, slug=category_slug, company__slug=comapny_slug) 

    # get a queryset of all the subcategories of the current category
    subcategories = category.subcategories.all()

    companies, products, categories = None, None, None
    page_obj_company, page_obj_product, page_obj_category = None, None, None
    page_number = request.GET.get('page')

    # Search by company name, category, subcategory, product name, model, or code.
    query = request.GET.get('q')
    if query:
        companies = Company.objects.filter(name__icontains=query) 
        categories = Category.objects.filter(name__icontains=query)
        subcategories = Subcategory.objects.filter(name__icontains=query)
        products = Product.objects.filter(
            Q(name__icontains=query)|
            Q(model__icontains=query)|
            Q(code__icontains=query)
        ).distinct() 

    # paginate the subcategories list
    paginator_subcategory = Paginator(subcategories, 12) # display 8 subcategories per page.
    page_obj_subcategory = paginator_subcategory.get_page(page_number)

    if companies:
        # paginate the companies list
        paginator_company = Paginator(companies, 12) # display 8 companies per page.
        page_obj_company = paginator_company.get_page(page_number)
    
    if categories:
        # paginate the categories list
        paginator_category = Paginator(categories, 12) # display 8 categories per page.
        page_obj_category = paginator_category.get_page(page_number)

    if products:
        # paginate the resulted products list
        paginator_product = Paginator(products, 12) # display 4 products per page.
        page_obj_product = paginator_product.get_page(page_number)

    context = { 'query':query,
                'subcategories':page_obj_subcategory, 
                'category':category, 
                'companies':page_obj_company,
                'categories':page_obj_category,
                'products':page_obj_product,
            }
    return render(request, 'product/subcategory_list.html', context)


def product_list(request, comapny_slug=None, category_slug=None, subcategory_slug=None):
    """
    Display the company category products list.
    """
    # get the current subcategory
    subcategory = get_object_or_404(Subcategory, slug=subcategory_slug, company__slug=comapny_slug, category__slug=category_slug) 

    # get a queryset of all the products of the current category
    products = subcategory.products.all()

    companies, categories, subcategories = None, None, None
    page_obj_company, page_obj_category, page_obj_subcategory = None, None, None
    page_number = request.GET.get('page')

    # Search by company name, category, subcategory, product name, model, or code.
    query = request.GET.get('q')
    if query:
        companies = Company.objects.filter(name__icontains=query) 
        categories = Category.objects.filter(name__icontains=query)
        subcategories = Subcategory.objects.filter(name__icontains=query)
        products = Product.objects.filter(
            Q(name__icontains=query)|
            Q(model__icontains=query)|
            Q(code__icontains=query)
        ).distinct() 

    # paginate the categories list
    paginator_product = Paginator(products, 12) # display 8 products per page.
    page_obj_product = paginator_product.get_page(page_number)
    
    if companies:
        # paginate the companies list
        paginator_company = Paginator(companies, 12) # display 8 companies per page.
        page_obj_company = paginator_company.get_page(page_number)
    
    if categories:
        # paginate the resulted products list
        paginator_category = Paginator(categories, 12) # display 8 categories per page.
        page_obj_category = paginator_category.get_page(page_number)

    if subcategories:
        # paginate the subcategories list
        paginator_subcategory = Paginator(subcategories, 12) # display 8 subcategories per page.
        page_obj_subcategory = paginator_subcategory.get_page(page_number)

    context = { 'query':query,
                'categories':page_obj_category, 
                'subcategory':subcategory, 
                'companies':page_obj_company,
                'subcategories':page_obj_subcategory,
                'products':page_obj_product,
            }
    return render(request, 'product/product_list.html', context)    



