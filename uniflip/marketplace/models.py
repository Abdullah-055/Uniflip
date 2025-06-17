from django.db import models
from django.contrib.auth.models import User

# Product model (existing)
class Product(models.Model):
    name = models.CharField("Product Name", max_length=255)
    description = models.TextField("Description", help_text="Provide product details.")
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    created_by = models.ForeignKey(User, verbose_name="Listed By", on_delete=models.CASCADE)
    created_at = models.DateTimeField("Listed On", auto_now_add=True)

    def __str__(self):
        return self.name

# Profile model (existing)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

# Order model (for Buy Page functionality)
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.product.name} by {self.buyer_name}"

# Contact Us model (fully fixed version)
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
