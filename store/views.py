from django.shortcuts import render
from .models import Product, Customer, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm


def actualizarUsuario(request, username, email):
    user = request.user
    user.username = username
    user.email = email
    user.save()
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
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registered")
            return redirect('home')
        else:
            messages.error(request, form.errors)
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'form': form})
    
        

@login_required
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        print(user_form.errors)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "Cuenta actualizada exitosamente.")
            return redirect('home')
        return render(request, 'update_user.html', {'user_form': user_form})

    
@login_required
def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Contraseña actualizada exitosamente.")
                login(request, current_user)
                return redirect('update_user')
            else:
                messages.error(request, form.errors)
                return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'form': form})
        
    
        
def update_info(request):
    if request.user.is_authenticated:
        current_user = request.user

    

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