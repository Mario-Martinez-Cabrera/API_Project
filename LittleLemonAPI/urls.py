from django.urls import path
from LittleLemonAPI import views

urlpatterns = [
    path('menu-items', views.menuitems_list),
]