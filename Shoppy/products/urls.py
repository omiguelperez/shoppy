from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/',
        views.ProductDetail.as_view(), name='detail'),
    url(r'^new/$', views.product_new, name='new'),
]
