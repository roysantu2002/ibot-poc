"""
Serializers for ldnsql APIs
"""
from ldnsql.models import SQLUser
from rest_framework import serializers


class SQLUserSerializer(serializers.ModelSerializer):
    """Serializer for ingredients."""

    class Meta:
        model = SQLUser
        fields = ['user_id', 'server_id', 'flag']
        read_only_fields = ['id']

    def create(self, validated_data):
        try:
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance
        except :
            raise serializers.ValidationError('User already exists.')