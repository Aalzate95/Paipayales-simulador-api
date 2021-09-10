from django.shortcuts import render
from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import SessionAuthentication



class PoolsViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    # authentication_classes=[SessionAuthentication]
    serializer_class = serializers.PoolsSerializer

    def get_queryset(self):
        pools = models.Pools.objects.all()
        return pools