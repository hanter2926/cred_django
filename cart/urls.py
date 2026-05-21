from django.urls import path
from .views import add_to_cart, cart_view, remove_cart_item

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_id>/', remove_cart_item, name='remove_cart'),
]