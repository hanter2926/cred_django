from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect('cart')

    total = sum(item.total_price() for item in cart_items)

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')

        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            mobile_no=mobile_no,
            address=address,
            total_amount=total
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()
        return redirect('my_orders')

    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})
