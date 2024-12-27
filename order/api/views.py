from .serializers import OrderSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class OrderCreateView(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response('order saved  succesffully')
