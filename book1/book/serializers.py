import re

from rest_framework import serializers

from book.models import User


def check_password(password):
    if re.match(r'^\d+$',password):
        raise serializers.ValidationError('密码不能纯数字')


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100,min_length=3,)
    password = serializers.CharField(max_length=100,min_length=5,validators=check_password())

    def validate_username(self,username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('用户名重复')
        else:
            return username

    def create(self,validated_data):
        User.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.password = validated_data.get('password',instance.password)
        instance.save()
        return instance

# class RequesView(APIView)
