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


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    title = product.name
    template = loader.get_template('product_detail.html')
    context = {
        'title': title,
        'product': product
    }
    return HttpResponse(template.render(context, request))
