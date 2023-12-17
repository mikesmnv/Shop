from django.urls import path
from .views import home, shop

urlpatterns = [
    path('home', home, name="home"),
    path('shop', shop, name="shop")
]