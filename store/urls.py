from django.urls import path
from .import views

urlpatterns=[
    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('process_order/',views.processOrder,name="process_order"),
    path('product/',views.product,name="product"),
    path('category/',views.category),
    path('register/',views.registerPage,name="registerPage"),
    path('login/',views.loginPage,name="loginPage"),
    path('logout/',views.logoutUser,name="logoutUser"),
]