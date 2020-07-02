from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .serializer import ProductSerializer, OrderSerializer
from .models import Product, Order


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('date')
    serializer_class = OrderSerializer

# def home(request):
#     return HttpResponse("Hello, world. You're building an invoice app")
