from django.urls import path
from LittleLemonAPI import views

urlpatterns = [
    path('categories', views.CategoryViews.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('cart/menu-items', views.CartView.as_view()),
    path('orders', views.OrderView.as_view()),
    path('orders/<int:pk>', views.SingleOrderView.as_view()),
    path('groups/manager/users', views.GroupViewSet.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'})),

    path('groups/delivery-crew/users', views.DeliveryCrewViewSet.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'})),
]

### for views not needed. To remember code. ### 
# path('menuitem/', views.menuitems_list),
    # path('menuitem/<int:id>', views.menuitem_detail),
    # path('cart/', views.cart_list),