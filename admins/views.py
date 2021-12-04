import json
import hmac
import hashlib
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GeometryModel, ProperitesModel, ProductModel, InventoryModel, StoreModel, OrdersModel
from .serializers import GeometrySerializer, ProperitesSerializer, ProductSerializer, InventorySerializer, StoreSerializer, AllStoreSerializer, OrderSerializer
import razorpay
client = razorpay.Client(auth=("rzp_test_exJ9gstv3NbI4x", "VLUIYlEdzMwF0p72hhwEuVWx"))
secret = b"VLUIYlEdzMwF0p72hhwEuVWx"
# Create your views here.


# TODO: Add Del Mtd
@api_view(['GET', 'POST'])
def create_and_get_products(request):
    """Create Products"""
    body_data = request.data
    if request.method == 'POST':
        serialized_data = ProductSerializer(data=body_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        products = ProductModel.objects.all()
        serialized_data = ProductSerializer(products, many=True)
        return Response(serialized_data.data)

@api_view(['GET', 'DELETE'])
def products_by_id(request, pk):
    if request.method == 'GET':
        queryset = ProductModel.objects.filter(id=pk)
        serialized = ProductSerializer(queryset, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        queryset = ProductModel.objects.filter(id=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def create_and_get_properties(request):
    """Create Properties"""
    body_data = request.data
    if request.method == 'POST':
        serialized_data = ProperitesSerializer(data=body_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        properties = ProperitesModel.objects.all()
        serialized_data = ProperitesSerializer(properties, many=True)
        return Response(serialized_data.data)

@api_view(['GET', 'POST'])
def create_and_get_geometry(request):
    """Create Geometry"""
    body_data = request.data
    if request.method == 'POST':
        serialized_data = GeometrySerializer(data=body_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        geometry = GeometryModel.objects.all()
        serialized_data = GeometrySerializer(geometry, many=True)
        return Response(serialized_data.data)

@api_view(['GET', 'POST'])
def create_and_get_inventory(request):
    """Create Inventory"""
    body_data = request.data
    if request.method == 'POST':
        serialized_data = InventorySerializer(data=body_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        inventory = InventoryModel.objects.all()
        serialized_data = InventorySerializer(inventory, many=True)
        return Response(serialized_data.data)

@api_view(['GET', 'POST'])
def create_and_get_store(request):
    """Create Store"""
    body_data = request.data
    if request.method == 'POST':
        serialized_data = StoreSerializer(data=body_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        store = StoreModel.objects.all()
        serialized_data = StoreSerializer(store, many=True)
        return Response(serialized_data.data)


@api_view(['GET'])
def get_all_stores(request):
    """Get all stores"""
    stores = StoreModel.objects.all()
    serialized_data = StoreSerializer(stores, many=True)
    all_stores = serialized_data.data
    geoArray= []
    prop_array = []
    store_array = []
    for store in all_stores:
        geo_id = store["geometry"]
        prop_id = store["properties"]
        resp = get_geo_by_id_func(geo_id)
        prop_resp = get_properties_by_id(prop_id)
        geoArray.append(resp.data)
        prop_array.append(prop_resp.data)
        store_array.append(store)
    return Response({"Geometry":geoArray, "Properties": prop_array, "Stores": store_array})

def get_geo_by_id_func(obj_id):
    queryset = GeometryModel.objects.filter(id=obj_id)
    serialized_geo = GeometrySerializer(queryset, many=True)
    return serialized_geo


def get_properties_by_id(obj_id):
    queryset = ProperitesModel.objects.filter(id=obj_id)
    serialized_properties = ProperitesSerializer(queryset, many=True)
    return serialized_properties

@api_view(['GET'])
def get_inventory_products(request, pk):
    """Get inventory products"""
    inventory = ProductModel.objects.filter(inventory_id=pk)
    serialized_data = InventorySerializer(inventory, many=True)
    all_products = []
    for product in serialized_data.data:
        product_id = product["id"]
        resp = get_product_by_id(product_id)
        print(resp.data[0])
        all_products.append(resp.data[0])
    # print(serialized_data.data[0]['id'])
    print(all_products)
    return Response(all_products)

@api_view(['GET'])
def get_properites(request, pk):
    prop = ProperitesModel.objects.filter(id=pk)
    serialized_data = ProperitesSerializer(prop, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def get_geo_by_id(request, pk):
    queryset = GeometryModel.objects.filter(id=pk)
    serialized = GeometrySerializer(queryset, many=True)
    return Response(serialized.data)

def get_product_by_id(obj_id):
    queryset = ProductModel.objects.filter(id=obj_id)
    serialized_data = ProductSerializer(queryset, many=True)
    return serialized_data

@api_view(['GET', 'POST'])
def make_payment(request):
    """Make Payments Using Razorpay"""
    if request.method == 'POST':
        body_data = request.data
        amount = body_data['amount']
        data = {
            "amount": amount,
             "currency": "INR"
        }

        payment = client.order.create(data=data)
        post_data = {
            "order_id":payment['id'],
            "items": body_data['items']
        }
        serialized_data = OrderSerializer(data=post_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(payment)
    if request.method == 'GET':
        orders = OrdersModel.objects.all()
        serialized_data = OrderSerializer(orders, many=True)
        return Response(serialized_data.data)

@api_view(['POST'])
def verify_sign(request):
    """Verify if a signature is valid or not"""
    body_data = request.data
    order_ID = body_data['razorpay_order_id']
    payment_id = body_data['razorpay_payment_id']
    signature = body_data['razorpay_signature']
    mystr = (order_ID + "|" + payment_id).encode()
    generated_signature = hmac.new(secret, mystr, hashlib.sha256).hexdigest()
    print(generated_signature)
    if generated_signature == signature:
        print("Sucess")
        return Response({"message":"Sucess"}, status=status.HTTP_200_OK)
    return Response({"message":"Failure"}, status=status.HTTP_400_BAD_REQUEST)
