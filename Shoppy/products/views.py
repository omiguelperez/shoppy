from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import ProductForm
from .mixins import LoginRequiredMixin
from .models import Product


class ProductList(ListView):
    model = Product


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product


@login_required(login_url='/auth-login/')
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


def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if action == 'signup':
            user = User.objects.create_user(
                username=username, password=password)
            login(request, user)
        elif action == 'login':
            user = authenticate(username=username, password=password)
            if not user:
                return redirect('/auth-login/')
            login(request, user)
        return redirect('/')
    return render(request, 'login/login.html', {})
