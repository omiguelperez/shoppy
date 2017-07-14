from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/',
        views.ProductDetail.as_view(), name='detail'),
    url(r'^new/', views.product_new, name='new'),
    url(r'^auth-login/', views.auth_login, name='auth_login'),
    url(r'^logout/', auth_views.logout,
        {'next_page': '/auth-login/'}, name='logout'),
]
