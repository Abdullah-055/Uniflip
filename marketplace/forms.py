from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Profile, Order, ContactMessage

class UserRegistrationForm(UserCreationForm):
    contact_number = forms.CharField(
        max_length=20, required=True, label='Contact Number'
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit)
        contact_number = self.cleaned_data.get('contact_number')
        user.profile.contact_number = contact_number
        user.profile.save()
        return user

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['buyer_name', 'phone', 'address']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message'] 
