
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Categorie(models.Model):
    sizes = (('small','small'),('large','large'))
    title = models.CharField(max_length=50,null=False)
    image = models.ImageField(null=True,blank=True)
    size = models.CharField(max_length=5,choices=sizes,default='small')
    def __str__(self):       
        return self.title

    @property 
    def imageURL(self):
        try:
            url=self.image.url #chk
        except:
            url=' '
        return url


class size(models.Model):
    title=models.CharField(max_length=10)

    def __str__(self):
        return (self.title)

class color(models.Model):
    title=models.CharField(max_length=10)

    def __str__(self):
        return (self.title)

class brand(models.Model):
    title=models.CharField(max_length=10)

    def __str__(self):
        return (self.title)

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    category=models.ForeignKey(Categorie,on_delete=models.SET_NULL,blank=True,null=True)
    price=models.FloatField()
    brand=models.ForeignKey(brand,on_delete=models.CASCADE)
    size=models.ForeignKey(size,on_delete=models.CASCADE)
    color=models.ForeignKey(color,on_delete=models.CASCADE)
    digital=models.BooleanField(default=False,null=True,blank=False)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):       
        return self.name

    @property 
    def imageURL(self):
        try:
            url=self.image.url #chk
        except:
            url=' '
        return url


class Order(models.Model):   
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_orderd=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital==False:
                shipping=True
        return shipping
    @property
    def get_cart_total(self):
        orderitems =self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
        
    @property
    def get_cart_items(self):
        orderitems =self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.product.price*self.quantity
        return total

class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    zipcode=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
        