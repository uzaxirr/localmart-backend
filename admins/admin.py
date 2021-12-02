from django.contrib import admin
from .models import GeometryModel, ProperitesModel, ProductModel, InventoryModel, StoreModel
# Register your models here.

admin.site.register(GeometryModel)
admin.site.register(ProperitesModel)
admin.site.register(ProductModel)
admin.site.register(InventoryModel)
admin.site.register(StoreModel)
