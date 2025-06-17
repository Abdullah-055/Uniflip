# marketplace/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Product, Profile, ContactMessage
from .forms import ProductForm, UserRegistrationForm, ContactForm, OrderForm


# ✅ Home page (fully cleaned version)
def home(request):
    return render(request, 'marketplace/home.html')


# ✅ Registration View
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        contact_number = request.POST['contact_number']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('marketplace:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('marketplace:register')

        user = User.objects.create_user(username=username, password=password1)
        Profile.objects.update_or_create(user=user, defaults={'contact_number': contact_number})
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect('marketplace:home')

    return render(request, 'registration/register.html')



# ✅ Product details page
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    seller = product.created_by

    profile, created = Profile.objects.get_or_create(user=seller)
    contact = profile.contact_number or "Not provided"

    return render(request, 'marketplace/product_detail.html', {
        'product': product,
        'seller': seller,
        'contact': contact
    })


# ✅ Listings page
def listings(request):
    products = Product.objects.all()
    is_admin = request.user.is_superuser
    return render(request, 'marketplace/listings.html', {'products': products, 'is_admin': is_admin})


# ✅ Add product (Sell page)
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            messages.success(request, 'Product successfully added!')
            return redirect('marketplace:listings')
    else:
        form = ProductForm()
    return render(request, 'marketplace/add_product.html', {'form': form})


# ✅ Logout view
def logout_view(request):
    logout(request)
    return redirect("marketplace:home")


# ✅ About Us page
def about_us(request):
    return render(request, 'marketplace/about_us.html')


# ✅ Contact Us page with success message
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Your message has been sent successfully! We will contact you shortly.")
            return redirect('marketplace:contact_us')
    else:
        form = ContactForm()
    return render(request, 'marketplace/contact_us.html', {'form': form})


# ✅ Buy product page (Order placement)
@login_required
def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            messages.success(request, '🎉 Your order has been placed successfully! Our seller will contact you soon.')
            return redirect('marketplace:listings')
    else:
        form = OrderForm()

    return render(request, 'marketplace/buy_product.html', {'form': form, 'product': product})
