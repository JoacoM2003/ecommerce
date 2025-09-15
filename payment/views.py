from django.shortcuts import render
from cart.cart import Cart
from store.models import Product
from .forms import ShippingForm, PaymentForm
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from store.models import Product

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
        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping

        for key in my_shipping:
            if not my_shipping[key]:
                messages.error(request, 'Please fill all the fields')
                return redirect('checkout')
        
        payment_form = PaymentForm()

        return render(request, 'payment/billing.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total, 'shipping_info': my_shipping, 'payment_form': payment_form})
    
@login_required
def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quantity()
        total = cart.get_total()

        payment_form = PaymentForm(request.POST or None)
        my_shipping = request.session.get('my_shipping')
        if request.user.is_authenticated:
            create_order = Order.objects.create(
                user=request.user,
                full_name=my_shipping['shipping_full_name'],
                email=my_shipping['shipping_email'],
                amount=total,
                shipping_address=f"{my_shipping['shipping_address']}, {my_shipping['shipping_depto']}, {my_shipping['shipping_city']}, {my_shipping['shipping_state']}, {my_shipping['shipping_zip_code']}, {my_shipping['shipping_country']}"
            )
            create_order.save()

            order_id = create_order.pk

            # Crear un OrderItem por cada producto y cantidad comprada
            for product in cart_products:
                product_id = product.id
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price
                quantity = quantities.get(str(product_id), 1)
                create_order_item = OrderItem.objects.create(
                    order_id=order_id,
                    product_id=product_id,
                    user=request.user,
                    quantity=quantity,
                    price=price
                )
                create_order_item.save()

            messages.success(request, 'Your order has been placed successfully')
            return redirect('home')     
        
    else:
        messages.error(request, 'Access Denied')
        return redirect('home')
    


    
