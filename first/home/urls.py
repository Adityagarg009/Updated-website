from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('order',views.order,name='order'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('coupons',views.coupons,name='coupon'),
    path('home',views.home,name='page'),
    path('sign',views.sign,name='sign'),
] 