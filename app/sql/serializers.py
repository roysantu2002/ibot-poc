"""
Serializers for ldnsql server APIs
"""
from .models import SQLServer
from rest_framework import serializers


class SQLServerSerializer(serializers.ModelSerializer):
    """Serializer for ingredients."""

    class Meta:
        model = SQLServer
        fields = ['server_id', 'is_active']
        read_only_fields = ['id']

    def create(self, validated_data):
        try:
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance
        except :
            raise serializers.ValidationError('Server already exists.')