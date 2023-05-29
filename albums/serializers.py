from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Album


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "name", "year", "user_id"]
        read_only_fields = ["user_id"]

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
