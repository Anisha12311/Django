from django.shortcuts import render

from .models import Productcart


def product_details(request):
    
    obj  = Productcart.objects.get(id=1)
    my_content = {
        'title': obj.title,
        'description': obj.description
    }
    
    return render(request, 'product/details.html', my_content)

# Create your views here.
