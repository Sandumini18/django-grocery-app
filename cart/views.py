from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart_item, Cart
from item.models import Item

@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = Cart_item.objects.filter(cart=cart)
    return render(request, 'cart/cart.html', {
        'items': items,
    })

@login_required
def add_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = Cart_item.objects.get_or_create(cart=cart, item=item)
    if cart_item:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:cart')

@login_required
def delete_from_cart(request, id):
    cart = Cart.objects.get(user=request.user)
    cart_item = Cart_item.objects.get(id=id)
    cart_item.delete()
    return redirect('cart:cart')