from django.shortcuts import render
from cart.cart import Cart
from store.models import Product
from .forms import ShippingForm, PaymentForm
from .models import ShippingAddress
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

def payment_sucess(request):
    return render(request, 'payment/payment_sucess.html')

@login_required
def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quantity()
    total = cart.get_total()
    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        
        return render(request, 'payment/checkout.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total, 'shipping_form': shipping_form})
    else:
        shipping_form = ShippingForm(request.POST or None)
        return render(request, 'payment/checkout.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total, 'shipping_form': shipping_form})
    
@login_required
def billing(request):
    if request.method == 'POST':
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quantity()
        total = cart.get_total()
        shipping_info = request.POST

        for key in shipping_info:
            if not shipping_info[key]:
                messages.error(request, 'Please fill all the fields')
                return redirect('checkout')
        
        payment_form = PaymentForm()

        return render(request, 'payment/billing.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total, 'shipping_info': shipping_info, 'payment_form': payment_form})

