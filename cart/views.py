from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from rem.models import OurworkModel
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    ourwork = get_object_or_404(OurworkModel, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(ourwork=ourwork, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    ourwork = get_object_or_404(OurworkModel, id=product_id)
    cart.remove(ourwork)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

