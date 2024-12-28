from django.urls import path
from .views import OrderCreateView, OrderListView,FarmerOrderListView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create_order'),
    path('all/<int:id>/', OrderListView.as_view(), name='all_orders'),
    path('my-orders/<int:id>/', FarmerOrderListView.as_view(), name='farmer_orders'),

]
