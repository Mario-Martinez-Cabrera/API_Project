from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from .models import MenuItem, Category, Cart, Order, OrderItem
from .serializers import MenuItemSerializer
from rest_framework import generics

# Create your views here.

def menuitems_list(request):
    menuitems = MenuItem.objects.all()
    serializer = MenuItemSerializer(menuitems, many=True)
    return JsonResponse(serializer.data)


#class MenuItemsView(generics.ListCreateAPIView):
#    queryset = MenuItem.objects.all()
#    serializer_class = MenuItemSerializer

#class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = MenuItem.objects.all()
#    serializer_class = MenuItemSerializer
