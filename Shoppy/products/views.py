from django.shortcuts import get_object_or_404, render

from .models import Product


def products(request):
    products = Product.objects.order_by('price')
    context = {'products': products}
    return render(request, 'products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'title': product.name,
        'product': product
    }
    return render(request, 'product_detail.html', context)
