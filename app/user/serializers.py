from rest_framework import serializers

class CreateAccountRequestSerializer(serializers.Serializer):

    full_name = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8)


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8)

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()