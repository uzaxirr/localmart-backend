"""Models for Store"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator

class GeometryModel(models.Model):
    """Model To hold Postion of store in map"""
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, default="Point")
    coordinates = ArrayField(models.DecimalField(max_digits=16, decimal_places=14), size=2)


class ProperitesModel(models.Model):
    """Model To hold details of store"""
    id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    store_adress = models.TextField(max_length=500)
    store_city = models.CharField(max_length=50)
    store_state = models.CharField(max_length=50, null = True)
    store_postal_code = models.BigIntegerField()

    def __str__(self) -> str:
        return self.store_name


class ProductModel(models.Model):
    """Model To hold details of product"""
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=9, decimal_places=2)
    inventory_id = models.ForeignKey('InventoryModel', on_delete=models.CASCADE, null=True)
    is_instock = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.product_name

class StoreModel(models.Model):
    """Model To hold details of store"""
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, default="FeatureCollection")
    geometry = models.OneToOneField(GeometryModel, on_delete=models.CASCADE)
    properties = models.OneToOneField(ProperitesModel, on_delete=models.CASCADE)
    inventory_id = models.ForeignKey('InventoryModel', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.properties.store_name

class InventoryModel(models.Model):
    """Model To hold details of inventory"""
    id = models.AutoField(primary_key=True)
    # product = models.ManyToManyField(ProductModel)
    store_id = models.ForeignKey(StoreModel, on_delete=models.CASCADE, null = True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null = True)
    
class OrdersModel(models.Model):
    """Model to hold Details of all orders"""
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=50)
    items = ArrayField(models.IntegerField(), null=True)
    store_id = models.ForeignKey(StoreModel, on_delete=models.CASCADE, null = True)

    def __str__(self) -> str:
        return self.order_id
        