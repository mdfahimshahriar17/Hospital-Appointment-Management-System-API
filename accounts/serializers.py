from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone', 'address', 'password', 'password2',]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords does not match."}
            )
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')

        user = User.objects.create_user(**validated_data)
        return user