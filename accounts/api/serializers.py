from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(
    #     style={'input-type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        style={'input-type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                "User with this email already exists")
        return value

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                "User with this username already exists")
        return value

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.get('password2')
        if pw != pw2:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validate_data):
        print(validate_data)
        user_obj = User(
            username=validate_data.get('username'),
            email=validate_data.get('email')
        )
        user_obj.set_password(validate_data.get('password'))
        user_obj.save()
        return user_obj
