from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from .models import MenuItem, Category, Cart, Order, OrderItem
from .serializers import MenuItemSerializer
from rest_framework import generics

# Create your views here.

@api_view(['GET', 'POST'])
def menuitems_list(request):
    if request.method == 'GET':
        menuitems = MenuItem.objects.all()
        serializer = MenuItemSerializer(menuitems, many=True)
        return JsonResponse({'menu items' : serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def menuitem_detail(request, id):

    try:
        menuitem = MenuItem.objects.get(pk=id)
    except MenuItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MenuItemSerializer(menuitem)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MenuItemSerializer(menuitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pass




#class MenuItemsView(generics.ListCreateAPIView):
#    queryset = MenuItem.objects.all()
#    serializer_class = MenuItemSerializer

#class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = MenuItem.objects.all()
#    serializer_class = MenuItemSerializer
