from rest_framework.serializers import ModelSerializer, ImageField

from . import models


class PoolsSerializer(ModelSerializer):
    class Meta:
        model = models.Pools
        fields = ["id", "name", "pool_type", "size"]