from django.urls import path
from . import views
from .views import register_view


app_name = 'marketplace'

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('listings/', views.listings, name='listings'),
    path('add/', views.add_product, name='add_product'),
    path('register/', register_view, name='register'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
]





    


