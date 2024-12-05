from django.shortcuts import render
from .models import Product, Customer, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages


def actualizarUsuario(request, username, email):
    user = request.user
    user.username = username
    user.email = email
    user.save()
    customer = Customer.get_by_email(request.POST['email-actual'])
    customer.email = email
    customer.name = request.POST['name']
    customer.phone = request.POST['phone']
    customer.address = request.POST['address']
    customer.save()
    messages.success(request, "Cuenta actualizada exitosamente.")

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        return render(request, 'signin.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')
        
@login_required
def signout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']

        if not username or not email:
            messages.error(request, "Por favor, complete todos los campos.")
            return redirect('signup')

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya existe.")
            return redirect('signup')

        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            login(request, user)
            Customer.create_and_save(name, email, phone, address)
            messages.success(request, "Cuenta creada exitosamente.")
            return redirect('home')
        except:
            messages.error(request, "Error al crear la cuenta.")
            return redirect('signup')
        
# def update(request):
#     return render(request, 'update.html')

@login_required
def update_user(request):
    if request.method == 'GET':
        customer = Customer.get_by_email(request.user.email)
        return render(request, 'update_user.html', {'user': request.user, 'customer': customer})
    elif request.method == 'POST':
        print(request.POST)
    try:
        username = request.POST['username']
        email = request.POST['email']
        if not username or not email or not request.POST["name"]:
            messages.error(request, "Por favor, complete todos los campos.")
            return redirect('update_user')
        elif User.objects.filter(username=username).exists():
            if username == request.user.username:
                actualizarUsuario(request, username, email)
                return redirect('home')
            else:
                messages.error(request, "El nombre de usuario ya existe.")
                return redirect('update_user')
        elif User.objects.filter(email=email).exists():
            if email == request.user.email:
                actualizarUsuario(request, username, email)
                return redirect('home')
            else:
                messages.error(request, "El correoentialActional ya existe.")
                return redirect('update_user')
        else:
            actualizarUsuario(request, username, email)
            return redirect('home')
    except:
        messages.error(request, "Error al actualizar la cuenta.")
        return redirect('update_user')
    
@login_required
def update_password(request):
    if request.method == 'GET':
        return render(request, 'update_password.html', {'user': request.user})
    elif request.method == 'POST':
        current_password = request.POST['current-password']
        if not request.user.check_password(current_password):
            messages.error(request, "La contraseña actual es incorrecta.")
            return redirect('update_password')
        elif request.POST['password1'] != request.POST['password2']:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('update_password')
        else:
            user = request.user
            user.set_password(request.POST['password1'])
            user.save()
            login(request, user)
            messages.success(request, "Contraseña actualizada exitosamente.")
            return redirect('home')
    
# @login_required
# def update_customer(request):
#     if request.method == 'GET':
#         print(request.user.email)
#         customer = Customer.get_by_email(email=request.user.email)
#         return render(request, 'update_customer.html', {'customer': customer})
#     elif request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         address = request.POST['address']
#         customer = Customer.get_by_email(request.user.email)
#         customer.name = name
#         customer.email = email
#         customer.phone = phone
#         customer.address = address
#         customer.save()
#         messages.success(request, "Cuenta actualizada exitosamente.")
#         return redirect('home')

def product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product.html', {'product': product})

def category(request, slug):
    try:
        category = Category.objects.get(name=slug)
        categories = Category.objects.all()
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'category': category, 'categories': categories, 'products': products})
    except:
        messages.error(request, "La categoría no existe.")
        return redirect('home')
    
def category_summary(request):
    return render(request, 'category_summary.html')