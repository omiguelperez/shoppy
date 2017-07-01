from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import ProductForm
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


def product_new(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return HttpResponseRedirect(
                reverse('product_detail', kwargs={'product_id': product.pk}))
    context = {
        'title': 'New product',
        'form': form
    }
    return render(request, 'product_new.html', context)
