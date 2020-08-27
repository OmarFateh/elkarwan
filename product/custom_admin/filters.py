from django.contrib.admin.filters import RelatedFieldListFilter

class ProductFilter(RelatedFieldListFilter):
    """
    """
    template = 'admin/product/dropdown_filter.html'
