from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quantity()
    total = cart.get_total()
    return render(request, 'cart.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total})

def add_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':    
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('quantity')
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_quantity)
        cart_count = cart.__len__()
        response = JsonResponse({"cart_count": cart_count})
        messages.success(request, 'Product added to cart')
        return response

def remove_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':    
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product=product)
        cart_count = cart.__len__()
        response = JsonResponse({"cart_count": cart_count})
        messages.success(request, 'Product removed from cart')
        return response

def update_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':    
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('quantity')
        product = get_object_or_404(Product, id=product_id)
        cart.update(product=product, quantity=product_quantity)
        response = JsonResponse({"quantity": product_quantity})
        return response
        return redirect('cart')
