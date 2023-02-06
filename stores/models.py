import secrets
from django.db import models
from users.models import Profile
from . paystack import PayStack

# Create your models here.
class Carousel(models.Model):
    slider = models.ImageField(upload_to='sliders')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.created_at)

class Banner(models.Model):
    banner_one = models.ImageField(upload_to='banners')
    banner_two = models.ImageField(upload_to='banners')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.created_at)

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=300)

    def __str__(self):
        return self.title




class Product(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100,default='No detail')
    ram = models.CharField(max_length=100,default='No detail')
    sim_slot = models.CharField(max_length=100,default='No detail')
    battery_capacity = models.CharField(max_length=100,default='No detail')
    sim_type = models.CharField(max_length=100,default='No detail')
    os = models.CharField(max_length=100,default='No detail')
    storage = models.CharField(max_length=100,default='No detail')
    screen_size = models.CharField(max_length=100,default='No detail')
    network = models.CharField(max_length=100,default='No detail')
    camera = models.CharField(max_length=100,default='No detail')
    description = models.CharField(max_length=250,null=True,blank=True)
    product_code = models.PositiveIntegerField(default=0,null=True,blank=True)
    price = models.PositiveIntegerField(max_length=100)
    discount_price = models.PositiveIntegerField(max_length=100,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    view_count = models.PositiveIntegerField(default=0,null=True,blank=True)
    warranty = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    similar_one = models.ImageField(upload_to= 'products',null=True,blank=True)
    similar_two = models.ImageField(upload_to= 'products',null=True,blank=True)
    similar_three = models.ImageField(upload_to= 'products',null=True,blank=True)
    image = models.ImageField(upload_to= 'products')
    image_one = models.ImageField(upload_to= 'products')
    image_two = models.ImageField(upload_to= 'products')
    image_three = models.ImageField(upload_to= 'products')
    image_four = models.ImageField(upload_to= 'products')
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title

    @property
    def get_percent(self):
        percentage = (self.discount_price) / self.price
        return percentage 


class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, null =True, blank =True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'cart :::: {str(self.id)}'

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, null =True, blank =True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null =True, blank =True)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'cart :::: {str(self.cart.id)} - cart product {self.id}'
ORDER_STATUS = (
    ('Order Received', 'Order Received'),
    ('Order Processing', 'Order Processing'),
    ('Order Shipped out', 'Order Shipped out'),
    ('Order Canceled', 'Order Canceled'),
    ('Order Completed', 'Order Completed'),
)
METHOD = (
    ('Paystack','Paystack'),
    ('Cash On Delivery','Cash On Delivery'),
    ('Bank Transfer','Bank Transfer')
)
class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete = models.CASCADE, null =True, blank =True)
    order_by = models.CharField(max_length=200)
    shipping_address = models.TextField()
    mobile = models.CharField(max_length=14)
    email = models.EmailField()
    discount= models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices = ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices= METHOD, default='Cash On Delivery')
    payment_completed = models.BooleanField(default=False,null=True,blank=True)
    ref = models.CharField(max_length=50,null=True, blank=True)

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            obj_with_sm_ref = Order.objects.filter(ref=ref)
            if not obj_with_sm_ref:
                self.ref= ref
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.order_status} :::: {str(self.id)}'



    def amount_value(self)->int:
        return self.amount * 100

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] /100 == self.amount:
                self.payment_completed = True
            self.save()

        if self.order_status == 'Order Completed':
            self.save()
            self.cart.delete()

        if self.payment_completed:
            return True
        return False


    
