from django.urls import path
from .views import cart_home, cart_add, cart_remove

app_name = 'shopping_cart'

urlpatterns = [
    path('', cart_home, name='cart'),
    path('add/', cart_add, name='add'),
    path('remove/', cart_remove, name='remove'),
]
