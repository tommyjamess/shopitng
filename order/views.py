from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from home.models import Setting
from products.models import *
from .models import *
from django.contrib import messages
import uuid
import random
import string 
import json 
import requests



# Create your views here.
def index(request):

    return HttpResponse('this is order')


@require_POST
@login_required(login_url='login')
def addtocart(request):
    url = request.META.get('HTTP_REFERER')
    thequantity = int(request.POST['quantity'])
    theprodid = request.POST['prodid']
    aprod = Product.objects.get(pk=theprodid)

    #check if 9the user has an existing cart
    cart = ShopCart.objects.filter(order_placed=False).filter(user__username = request.user.username)

    if cart: #an existiing cart is noticed
        prodchecker = ShopCart.objects.filter(product_id = aprod.id, quantity=thequantity, user__username= request.user.username).first()

        if prodchecker: #product exists in cart,  increment it
            prodchecker.quantity += thequantity
            prodchecker.save()
            messages.success(request, "product added to shopcart")
            return redirect(url)

        else: #product is not in the cart, add it
            anitem = ShopCart()
            anitem.product=aprod
            anitem.user=request.user
            anitem.order_code=cart[0].order_code
            anitem.quantity=thequantity
            anitem.order_placed=False
            anitem.save()

    else: #create a new cart, generate order code
        ordercode = str(uuid.uuid4())
        newcart = ShopCart()
        newcart.product = aprod
        newcart.user=request.user
        newcart.order_code=ordercode
        newcart.quantity=thequantity
        newcart.order_placed=False
        newcart.save()
    
    messages.success(request, 'Product addd to Shopcart')
    return redirect(url)



@login_required(login_url='login')
def cart(request):
    shopcart = ShopCart.objects.filter(order_placed=False).filter(user__username=request.user.username)
    brand = Brand.objects.all()
    cat = Category.objects.all()

    subtotal=0
    shippingfee =0
    vat = 0
    total = 0

    for item in shopcart:
        subtotal +=item.product.price * item.quantity
        

    #shipping rules: 8% fees to all orders above 150. 0 fees to oorders lower
    if subtotal > 150:
        shippingfee = 0.08 * subtotal
    else:
        shippingfee = 0
    
    vat = 0.075 * subtotal

    total = subtotal + shippingfee + vat

    context = {
        'cart': shopcart,
        'subtotal': subtotal,
        'shipping': shippingfee,
        'vat': vat,
        'total': total,
        'brands': brand,
        'cat': cat,
}

    return render(request, 'cart.html', context)



@login_required(login_url='login')
def checkout(request):
    shopcart = ShopCart.objects.filter(order_placed=False).filter(user__username=request.user.username)
    profile = UserProfile.objects.get(user__username = request.user.username)
    setting = Setting.objects.get(pk=1)

    subtotal=0
    shippingfee =0
    vat = 0
    total = 0

    for item in shopcart:
        subtotal +=item.product.price * item.quantity
        

    #shipping rules: 8% fees to all orders above 150. 0 fees to oorders lower
    if subtotal > 150:
        shippingfee = 0.08 * subtotal
    else:
        shippingfee = 0
    
    vat = 0.075 * subtotal

    total = subtotal + shippingfee + vat

    context = {
        'cart': shopcart,
        'subtotal': subtotal,
        'shipping': shippingfee,
        'vat': vat,
        'total': total,
        'profile': profile,
        'setting': setting,
}

    return render(request, 'checkout.html', context)

@login_required(login_url='login')
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, 'Item deleted from ShopCart')
    return redirect('order:cart')


@require_POST
@login_required(login_url='login')
def placeorder(request):
    api_key = 'sk_test_d3a8ed0644189273d85e8ac97f71b0e02507ac68'
    url = 'https://api.paystack.co/transaction/initialize'
    callback_url ='http://127.0.0.1:8000/order/ordercompleted/'
    ordercode = request.POST['order_number']
    autogen_ref = ''.join(random.choices(string.digits + string.ascii_letters, k=8))
    current_user = User.objects.get(username = request.user.username)
    user = UserProfile.objects.get(user_id = current_user.id)
    total = float(request.POST['amount']) * 100

    headers = {'Authorization': f'Bearer {api_key}'}
    data = {'reference': autogen_ref, 'amount': int(total), "currency": "NGN", 'order_number':ordercode, 'email':user.email, 'callback_url':callback_url}

    #making a request to paystack
    try:
        r =requests.post(url, headers=headers, json=data)
    except Exception:
        messages.error(request, 'Network busy, please try again in few minutes. Thank You!')
    else:
        #create an order
        transback = json.loads(r.text)

        rd_url = transback['data']['authorization_url']
        theuser = UserProfile.objects.filter(user=request.user).first()
        order = Order()
        order.user=current_user
        order.first_name=theuser.user.first_name
        order.last_name=theuser.user.last_name
        order.phone=theuser.phone
        order.city=theuser.city
        order.address=theuser.address
        order.state=theuser.state
        order.country=theuser.country
        order.email=theuser.email
        order.order_code=ordercode
        order.payment_code= autogen_ref
        order.total=total 
        order.order_placed= True 
        order.save()
        

        return redirect(rd_url)

    return redirect('order:checkout')


@login_required(login_url='login')
def ordercompleted(request):

    return render(request, 'ordercompleted.html')