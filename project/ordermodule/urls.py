from django.urls import path
from ordermodule import views

urlpatterns = [
    path('category/', views.category),
    path('items/<str:cate_name>', views.items, name="items"),
    path('search/', views.searchItem),
    path('itemdetails/<int:item_id>', views.itemDetails, name="itemDetails"),
    path('checkout/', views.checkout),
    path('invoice/', views.invoice),
    path('orderdetails/', views.orderDetails),
    path('preview/',views.Preview),
    path('download/',views.Download),
]
