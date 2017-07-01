from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.products, name='products'),
    url(r'^detail/(?P<product_id>[0-9]+)/',
        views.product_detail, name='product_detail'),
    url(r'^new/$', views.product_new, name='product_new'),
]
