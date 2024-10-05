from django.db import models
import uuid
from django.conf import settings


# Create your models here. Here will be the Category and Product models for registering products purchased in the store.

class Phone(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    phone = models.CharField(max_length=12, blank=True, null=True)


class Email(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(blank=True, null=True)

class Supliers(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sup_name = models.CharField(max_length=80)
    ICO = models.CharField(max_length=8, blank=True, null=True)
    ICDPH = models.CharField(max_length=12)
    tel = models.ForeignKey(Phone, on_delete=models.CASCADE, name='phone', blank=True, null=True)
    email = models.ForeignKey(Email, on_delete=models.CASCADE, name='email', blank=True, null=True)
    ulica = models.CharField(max_length=100, blank=True, null=True)
    dom = models.CharField(max_length=10, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self) -> str:
        return self.sup_name



class Factura(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    factura_number = models.CharField(max_length=100, blank=True, null=True)
    factura_date = models.DateField(blank=True, null=True)
    supliers = models.ForeignKey(Supliers, on_delete=models.CASCADE, name='supliers', blank=True, null=True)

    def __str__(self) -> str:
        return self.factura_number



class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

    

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    product_code = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_dph = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dph = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, name='factura')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return self.product_name

    class Meta:
        verbose_name_plural = "Products"




        
