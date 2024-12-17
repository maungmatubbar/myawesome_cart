from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('product-view/', views.product_view, name="Search"),
    path('checkout/', views.checkout, name="Checkout"),
    path('cart/', views.checkout, name="cart"),
]
