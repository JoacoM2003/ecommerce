from store.models import Product
class Cart():
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            self.session['cart'] = {}
            self.cart = self.session['cart']
        else:
            self.cart = self.session['cart']
    
    def add(self, product, quantity):
        product_id = str(product.id)
        quantity = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(quantity)
        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quantity(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product.id)
        quantity = str(quantity)
        self.cart[product_id] = int(quantity)
        self.session.modified = True
        return self.cart
    
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

        return self.cart
    
    def get_total(self):
        total = 0
        for product in self.get_prods():
            if product.is_sale:
                total += product.sale_price * self.cart[str(product.id)]
            else:
                total += product.price * self.cart[str(product.id)]
        return total