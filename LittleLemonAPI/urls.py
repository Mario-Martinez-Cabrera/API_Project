from django.urls import path
from LittleLemonAPI import views

urlpatterns = [
    path('menuitem/', views.menuitems_list),
    path('menuitem/<int:id>', views.menuitem_detail),
]