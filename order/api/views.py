from .serializers import OrderSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from order.models import Order


class OrderCreateView(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response('order saved  succesffully')


class FarmerOrderListView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(farmer=user)
        return queryset


#
# class OrderListView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()


class OrderListView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'id'
    queryset = Order.objects.all()
