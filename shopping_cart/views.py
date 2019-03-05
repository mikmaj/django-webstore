from django.shortcuts import render, redirect
from django.contrib import messages
from webstore.models import StoreItem
from .models import ShoppingCart


def cart_home(request):
    cart_obj, new_obj = ShoppingCart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    return render(request, "shopping_cart/shopping_cart.html", {"cart": cart_obj})


def cart_add(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id is not None:
            product_obj = StoreItem.objects.get(id=product_id)
            cart_obj, new_obj = ShoppingCart.objects.new_or_get(request)
            cart_obj.products.add(product_obj)
            messages.success(request, 'Item added to cart!')
    return redirect("webstore-home")


def cart_remove(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        product_obj = StoreItem.objects.get(id=product_id)
        cart_obj, new_obj = ShoppingCart.objects.new_or_get(request)
        cart_obj.products.remove(product_obj)
        messages.success(request, 'Item removed!')
    return redirect(request.META['HTTP_REFERER'])
