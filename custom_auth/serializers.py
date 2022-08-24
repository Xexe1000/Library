from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()

    def validate_login(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('login already used')
        return value

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as b:
            raise serializers.ValidationError(b)
        return value

    def create(self, validated_data):
        user = User.objects.create(username=validated_data.get('login'))
        user.set_password(validated_data.get('password'))
        user.save()
        return user
