"""
Serializers for ldnsql server APIs
"""
from rest_framework import serializers

from .models import SQLServer


class SQLServerSerializer(serializers.ModelSerializer):
    """Serializer for ingredients."""

    class Meta:
        model = SQLServer
        fields = ['id' ,'server_id', 'is_active']
        read_only_fields = ['id']
    # server_id = serializers.CharField(required=True, min_length=8)

    def create(self, validated_data):
        try:
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance
        except :
            raise serializers.ValidationError('Server already exists.')