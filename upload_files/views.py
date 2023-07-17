from rest_framework import generics
from .models import UserSession
from .serializers import UserSessionSerializer

class UserSessionCreateView(generics.CreateAPIView):
    queryset = UserSession.objects.all()
    serializer_class = UserSessionSerializer