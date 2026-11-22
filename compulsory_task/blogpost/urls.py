from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.urls import path
from . import views

urlpatterns = [

    path(
        'home/',
        views.home,
        name='home'
    ),

    path(
        'post/',
        views.post,
        name='post'
    ),

    path(
        'blogpost/',
        views.blogpost,
        name='blogpost'
    ),

    path(
        'payment/',
        views.payment,
        name='payment'
    ),

    path(
        'membership/',
        views.member,
        name='membership'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'logout-page/',
        views.logout_user,
        name='logout_page'
    ),

    path(
    'purchase-success/',
    views.purchase_success,
    name='purchase_success'
    ),

    path(
    'cart/',
    views.cart,
    name='cart'
),


path(
    'add-to-cart/<str:product_name>/',
    views.add_to_cart,
    name='add_to_cart'
),

path(
    'clear-cart/',
    views.clear_cart,
    name='clear_cart'
),

path(
    'remove-from-cart/<str:product_name>/',
    views.remove_from_cart,
    name='remove_from_cart'
),

path(
    'update-quantity/<str:product_name>/',
    views.update_quantity,
    name='update_quantity'
),
]