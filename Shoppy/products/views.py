from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import ProductForm
from .models import Product


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


def product_new(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return HttpResponseRedirect(
                reverse('products:detail', kwargs={'pk': product.pk}))
    context = {
        'title': 'New product',
        'form': form
    }
    return render(request, 'product_new.html', context)
