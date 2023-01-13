"""
Serializers for ldnsql APIs
"""
from sqluser.models import SQLUser
from rest_framework import serializers


class SQLUserSerializer(serializers.ModelSerializer):
    """Serializer for ingredients."""

    class Meta:
        model = SQLUser
        fields = ['user_id', 'server', 'flag']
        read_only_fields = ['id']

    def create(self, validated_data):
        try:
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance
        except :
            raise serializers.ValidationError('User already exists.')

    # def update(self, instance, validated_data):
    #    print(validated_data)
    #    instance.user_id = validated_data.get('user_id', instance.server)
    #    instance.server = validated_data.get('server', instance.server)
    #    instance.flag = validated_data.get('flag', instance.flag)
    #    print(instance)
    #    try:
    #         instance.save()
    #         return instance
    #    except :
    #         raise serializers.ValidationError('something went wrong.')
class UpdateUserSerializer(serializers.ModelSerializer):
    """
    Serializer to update the information of a logged-in user
    """

    class Meta:
        model = SQLUser
        fields = ['server', 'flag']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        print(validated_data)
        instance.server = validated_data.get('server', instance.server)
        instance.flag = validated_data.get('flag', instance.flag)
        # user = self.context["request"].user
        # if user.pk != instance.pk:
        #     raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        # instance.firstname = validated_data["firstname"]
        # instance.lastname = validated_data["lastname"]
        # instance.phonenumber = validated_data["phonenumber"]
        instance.save()
        return instance