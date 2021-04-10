from django.shortcuts import render ,redirect
from django.http import JsonResponse
import json   
import datetime

from .forms import CreateUserForm
from .models import *
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import productFilter


#create ur views here
def registerPage(request):
    if request.user.is_authenticated:
        return redirect ('store')
    else: 
        form=CreateUserForm()

        if (request.method)=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'account created by '+ user)
                return redirect('loginPage')

        context={'form':form}
        return render(request,'store/register.html',context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect ('store')
    else: 
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return  redirect('store')
            else:
                messages.info(request,'username or password is incorrect')
        context={}
        return render(request,'store/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect ('loginPage')

@login_required(login_url='loginPage')

def store(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems=order['get_cart_items']

    products=Product.objects.all()[:6]
    categories = Categorie.objects.all()
    context={'categories':categories, 'products':products,'cartItems':cartItems}
    return render(request,'store/store.html',context)

def category(request):
    categoryId = request.GET.get('category')
    print(request.GET)
    if categoryId is not None:
        products = Product.objects.filter(category = categoryId)
    else:
        products = Product.objects.all()

    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems=order['get_cart_items']

    context={'products':products,'cartItems':cartItems}

    return render(request,'store/category.html',context)
    
def product(request):   
    product = Product.objects.all()
    product_filter = productFilter(request.GET,queryset=product)
    products = product_filter.qs
    
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems=order['get_cart_items']
    
    cartItems=order.get_cart_items
    context = {'product_filter':product_filter,'products':products,'cartItems':cartItems}
    return render(request,'store/product.html',context)

@login_required(login_url='loginPage')
def cart(request):

    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems=order['get_cart_items']

    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)

@login_required(login_url='loginPage')
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]       
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems=order['get_cart_items']

    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/checkout.html',context)

@login_required(login_url='loginPage')
def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']

    print('Action:',action)
    print('productId:',productId)

    customer = request.user.customer
    product=Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)

    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)

    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity-1)

    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)
    s
@login_required(login_url='loginPage')
def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)

    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        total=float(data['form']['total'])
        order.transaction_id=transaction_id

        if total==order.get_cart_total:
            order.complete=True
        order.save()

        if order.shipping==True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],

                )     
    else:
        print('User is not logged in..')

    return JsonResponse('Payment complete!',safe=False)