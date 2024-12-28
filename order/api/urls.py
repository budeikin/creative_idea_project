from django.urls import path
from .views import OrderCreateView, OrderListView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create_order'),
    path('all/<int:pk>/', OrderListView.as_view(), name='all_orders'),
    # path('my-orders/<int:pk>/', FarmerOrderListView.as_view(), name='farmer_orders'),

]
