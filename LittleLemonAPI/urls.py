from django.urls import path
from LittleLemonAPI import views

urlpatterns = [
    path('menuitems', views.menuitems_list),
]