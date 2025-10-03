from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.homes.views import HomeAPIView

router = DefaultRouter()
router.register(r'homes', HomeAPIView, basename='homes')

urlpatterns = [
    path('', include(router.urls)),
]
