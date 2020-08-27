# -*- coding: utf-8 -*-

def arabic_slugify(string):
    """
    Slugify a given string. 
    """
    string = string.replace(" ", "-")
    string = string.replace(",", "-")
    string = string.replace("(", "-")
    string = string.replace(")", "")
    string = string.replace("؟", "")
    string = string.replace("!", "")
    return string

def unique_slug_generator(instance, new_slug=None):
    """
    Generate a unique slug of given instance.
    """
    # check if the given arguments have a value of new slug
    # if yes, assign the given value to the slug field. 
    if new_slug is not None:
        slug = new_slug
    # if not, generate a slug using arabic slugify function.
    else:
        slug = arabic_slugify(instance.name)
    # get the instance class. 
    Klass = instance.__class__
    # check if there's any item with the same slug.
    qs = Klass.objects.filter(slug=slug).order_by('-id')    
    qs_exists = qs.exists()
    # if yes, generate a new slug of a random string and return recursive function with the new slug.
    if qs_exists:
        new_slug = f'{slug}-{qs.first().id}'
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
