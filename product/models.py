# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse

from django_resized import ResizedImageField

from .utils import unique_slug_generator


def company_image_upload_to(instance, filename):
    """
    Upload the company image into the path and return the uploaded image path.
    """
    path = f"companies/{instance.name}/{filename}"
    return path

def category_image_upload_to(instance, filename):
    """
    Upload the category image into the path and return the uploaded image path.
    """
    path = f"companies/{instance.company}/{instance.name}/{filename}"
    return path

def product_image_upload_to(instance, filename):
    """
    Upload the product image into the path and return the uploaded image path.
    """
    path = f"companies/{instance.company}/{instance.category}/{instance.name}/{filename}"
    return path

class Company(models.Model):
    """
    Company model.
    """
    name       = models.CharField(max_length=255, unique=True)
    image      = ResizedImageField(size=[280, 120], quality=100, upload_to=company_image_upload_to)
    slug       = models.SlugField(unique=True, allow_unicode=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp  = models.DateTimeField(auto_now_add=True)   

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        # return the company name
        return self.name  

    def save(self, *args, **kwargs):
        # Override the save method and slugify the company name before saving. 
        if not self.slug:
            self.slug = unique_slug_generator(self)
        super(Company, self).save(*args, **kwargs)

    def get_absloute_url(self):
        # Return the absloute url of company categories. 
        return reverse('product:category-list', kwargs={'slug':self.slug})  


class Category(models.Model):
    """
    Category model.
    """
    ICON_TYPE = (
        ("tools", "أدوات"),  
        ("hammer", "شاكوش"),
        ("toolbox", "صندوق أدوات"),
        ("screwdriver", "مفك"),
        ("wrench", "مفتاح"),  
    )  

    name       = models.CharField(max_length=255)
    image      = models.ImageField(upload_to=category_image_upload_to, null=True, blank=True)
    icon_type  = models.CharField('Icon', max_length=15, choices=ICON_TYPE)
    company    = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='categories')
    slug       = models.SlugField(unique=True, allow_unicode=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp  = models.DateTimeField(auto_now_add=True)   

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        # return the category name
        return self.name 

    def save(self, *args, **kwargs):
        # Override the save method and slugify the category name before saving. 
        if not self.slug:
            self.slug = unique_slug_generator(self)
        super(Category, self).save(*args, **kwargs)     
     
class Product(models.Model):
    """
    Product model.
    """
    name       = models.CharField(max_length=255)
    image      = ResizedImageField(size=[160, 160], quality=100, upload_to=product_image_upload_to)
    company    = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    category   = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') 
    model      = models.CharField(max_length=255)
    code       = models.CharField(max_length=255, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp  = models.DateTimeField(auto_now_add=True)     

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        # return the product name
        return self.name