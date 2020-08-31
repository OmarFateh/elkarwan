from django import forms

from product.models import Category, Subcategory, Product

class ProductAdminFormMixin(forms.ModelForm):
    """
    Product admin model form mixin.
    """
    class Meta:
        model  = Product
        fields = ['company', 'category', 'subcategory']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()
        
        if 'company' in self.data:
            try:
                company_id = int(self.data.get('company'))
                self.fields['category'].queryset = Category.objects.filter(company_id=company_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.company.categories.order_by('name')

        self.fields['subcategory'].queryset = Subcategory.objects.none()
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.order_by('name')    


class ProductAdminForm(ProductAdminFormMixin, forms.ModelForm):
    """
    Product admin model form.
    """
    class Meta:
        model  = Product
        fields = ['name', 'image', 'company', 'category', 'subcategory', 'model', 'code']


class ProductFilterForm(ProductAdminFormMixin, forms.ModelForm):
    """
    Product admin filter model form.
    """
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False) 
    
    class Meta:
        model  = Product
        fields = ['company', 'category']


class SubcategoryAdminForm(forms.ModelForm):
    """
    Subcategory admin model form.
    """    
    class Meta:
        model  = Subcategory
        fields = ['name', 'company', 'category']
