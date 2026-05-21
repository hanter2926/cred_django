from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def cart_view(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.total_price()

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def remove_cart_item(request, cart_id):

    cart_item = get_object_or_404(Cart, id=cart_id)

    cart_item.delete()

    return redirect('cart')
