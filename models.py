from django.db import models
from user.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='회원')
    products = models.ManyToManyField(
        'product.Product', through='OrderProduct', verbose_name='상품명')
    total_price = models.IntegerField(verbose_name='총 가격')
    ordered_date = models.DateTimeField(
        auto_now_add=True, verbose_name='주문 날짜')

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'orders'


class OrderProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='주문갯수')

    class Meta:
        db_table = 'order_products'





from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='상품명')
    manufacturer = models.CharField(max_length=100, verbose_name='제조사')
    stock = models.IntegerField(verbose_name='재고수량')
    unit_price = models.IntegerField(verbose_name='단가')
    expiration_date = models.DateField(auto_now_add=True, verbose_name='유통기한')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = '상품'
        verbose_name_plural = '상품'




from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45, verbose_name='회원이름')
    email = models.EmailField(unique=True, verbose_name='이메일')
    password = models.CharField(max_length=100, verbose_name='비밀번호')
    phone_number = models.CharField(
        max_length=50, unique=True, verbose_name='전화번호')
    address = models.CharField(max_length=200, verbose_name='주소')
    gender = models.CharField(max_length=30, verbose_name='성별')
    register_date = models.DateField(auto_now_add=True, verbose_name='등록일')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'
        verbose_name = '회원'
        verbose_name_plural = '회원'