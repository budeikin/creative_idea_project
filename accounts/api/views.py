from rest_framework import generics, status
from .serializers import RegisterionSerializer, UserSerializer
from rest_framework.response import Response


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email': serializer.validated_data['email']
            }
        return Response('registered succesffully')
