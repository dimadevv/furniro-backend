from rest_framework import viewsets

from apps.homes.models import Home
from apps.homes.serializers import HomeSerializers


class HomeAPIView(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializers
    pagination_class = None

