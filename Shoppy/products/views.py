from django.http import HttpResponse
from django.template import loader

from .models import Product


def products(request):
    products = Product.objects.order_by('price')
    template = loader.get_template('products.html')
    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))
