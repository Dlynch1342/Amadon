from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^products$', views.add_product)
    url(r'buy$', views.buy),
    url(r'amadon/checkout$', views.checkout),
]
