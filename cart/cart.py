from store.models import Product, Profile
class Cart():
    def __init__(self, request):
        self.session = request.session
        self.request = request
        cart = request.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    
    def add(self, product, quantity):
        product_id = str(product.id)
        quantity = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(quantity)
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("'", '"')
            current_user.update(old_cart=str(carty))

    def db_add(self, product, quantity):
        product_id = str(product)
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