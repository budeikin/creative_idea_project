from rest_framework import generics, status
from .serializers import RegisterionSerializer
from rest_framework.response import Response

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterionSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email': serializer.validated_data['email']
            }
        return Response('registered succesffully')
