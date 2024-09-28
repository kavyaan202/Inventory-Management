# inventory/urls.py

from django.urls import path
from .views import ItemViewSet, UserRegisterView, UserLoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
] + router.urls
