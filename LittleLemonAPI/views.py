from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse, JsonResponse
from .models import MenuItem, Cart, Order, OrderItem, Category
from .serializers import MenuItemSerializer, CartSerializer, OrderItemSerializer, OrderSerializer, CategorySerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from django.shortcuts import  get_object_or_404
from django.contrib.auth.models import Group, User
from rest_framework import viewsets

# Create your views here.

class CategoryViews(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields = ['category__title']
    ordering_fields = ['price', 'inventory']

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
    

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.all().filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        Cart.objects.all().filter(user=self.request.user).delete()
        return Response("ok")
    



### Not needed but nice to have and to remember the code ###
# @api_view(['GET', 'POST'])
# def menuitems_list(request):
#     if request.method == 'GET':
#         menuitems = MenuItem.objects.all()
#         serializer = MenuItemSerializer(menuitems, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MenuItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def menuitem_detail(request, id):

#     try:
#         menuitem = MenuItem.objects.get(pk=id)
#     except MenuItem.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = MenuItemSerializer(menuitem)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = MenuItemSerializer(menuitem, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         menuitem.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def cart_list(request):
#     if request.method == 'GET':
#         cartitems = Cart.objects.all()
#         serializer = CartSerializer(cartitems, many=True)
#         return Response(serializer.data)
