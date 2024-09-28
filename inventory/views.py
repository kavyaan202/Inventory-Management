# inventory/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Item
from .serializers import ItemSerializer, UserSerializer
import logging

logger = logging.getLogger(__name__)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            logger.info("Item created successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Item creation failed: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("User registered successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("User registration failed: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            logger.info("User logged in successfully.")
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        logger.error("Invalid credentials for user: %s", username)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
