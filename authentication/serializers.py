from rest_framework import serializers

from authentication.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'main_currency', 'token')

        read_only_fields = ['token']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if User.objects.filter(email=email).exists() and User.objects.filter(username=username).exists():
            raise serializers.ValidationError({username, 'Username already in use'}, {email, 'Email already in use'})
        elif User.objects.filter(email=email).exists():
            raise serializers.ValidationError({email, 'Email already in use'})
        elif User.objects.filter(username=username).exists():
            raise serializers.ValidationError({username, 'Username already in use'})
        return super().validate(attrs)

    def create(self, validated_data):
        new_user = User.objects.create(**validated_data)
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'token')

        read_only_fields = ['token']
