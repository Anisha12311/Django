from django.http import HttpResponse
from django.shortcuts import render


def home_view(request,*args, **kwargs):
    my_context = {
        "name": "Ayn",
        "list":[12,12,32,4,5,6,7,3],
        "test": "hello  &lt;i&gt;my &lt;/i&gt; world Hello &lt;i&gt;my&lt;/i&gt; World!"
    }
    return render(request, 'home_view.html', my_context)    
    
def contact_view(request,*args, **kwargs):
    return HttpResponse("<h1>Hello contact Django</h2>")
    
    
def about_view(request,*args, **kwargs):
    return HttpResponse("<h1>Hello  about Django</h2>")
    
    
def social_view(request,*args, **kwargs):
    return HttpResponse("<h1>Hello social Django</h2>")
    
    
    