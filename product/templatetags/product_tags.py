from django import template

register = template.Library()

@register.simple_tag
def relative_url(value, field_name, urlencode=None):
    """
    Return the URL-encoded querystring for the current page
    updating the params with the key/value pairs passed to the tag.
    
    E.g: given the value=1 , field_name='page' , urlencode='http://127.0.0.1:8000/?page=1&filter=&title='
    {% relative_url 1 'page' request.GET.urlencode %} outputs ?page=1&filter=&title=

    """
    url = '?{}={}'.format(field_name, value)    #?page=1
    if urlencode:
        querystring = urlencode.split('&')  #['http://127.0.0.1:8000/jobs/favourite/?page=1', 'filter=', 'title=',]
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)  #['filter=', 'title=',]
        encoded_querystring = '&'.join(filtered_querystring) #filter=&title=
        url = '{}&{}'.format(url, encoded_querystring)   #?page=1&filter=&title=
    return url 


@register.simple_tag
def get_max(*num):
    """
    Take numbers and return their max.
    """
    return max(num) 
