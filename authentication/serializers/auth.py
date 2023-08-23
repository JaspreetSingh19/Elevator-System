from rest_framework import serializers
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken


from account.models import User
from common.messages import VALIDATION, MAX_LENGTH, MIN_LENGTH


class LoginSerializer(serializers.ModelSerializer):
    """
    used to verify the login credentials and return the login response
    """
    email = serializers.EmailField(
        required=True, allow_blank=False, error_messages=VALIDATION['email']
    )
    password = serializers.CharField(
        min_length=MIN_LENGTH['password'], max_length=MAX_LENGTH['password'], write_only=True, required=True,
        trim_whitespace=False, error_messages=VALIDATION['password']
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = User.objects.filter(email=email).first()

        if not user:
            raise serializers.ValidationError({'credentials': VALIDATION['invalid_credentials']})

        if not user.check_password(password):
            raise serializers.ValidationError({'credentials': VALIDATION['invalid_credentials']})

        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        """
        Generate the access and refresh tokens for the authenticated user
        """
        user = User.objects.filter(email=validated_data['email']).first()
        refresh = RefreshToken.for_user(user)

        user_token = User.objects.get(id=user.id)
        user_token.token = str(refresh.access_token)
        user_token.save()

        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

    class Meta:
        """
        Class Meta for SigninSerializer
        """
        model = User
        fields = ['email', 'password']


class LogoutSerializer(serializers.Serializer):
    """
    Serializer for user logout
    It blacklisted the refresh token after
    the authenticated user is logged-out
    """
    refresh = serializers.CharField(max_length=255)

    def validate(self, attrs):
        """
        Validate the refresh token from the user
        :param attrs: refresh
        :return: attrs
        """
        try:
            token = RefreshToken(attrs['refresh'])
            token_type = token.__class__.__name__
            if token_type != 'RefreshToken':
                raise serializers.ValidationError(VALIDATION['Invalid'])
            attrs['refresh_token'] = token
        except (InvalidToken, TokenError) as e:
            raise serializers.ValidationError(str(e))
        return attrs

    def create(self, validated_data):
        """
        Override create method to add refresh token
        to blacklist
        :param validated_data: refresh
        :return: success and error message
        """
        refresh_token = self.validated_data['refresh_token']
        refresh_token.blacklist()
        return {'success': True}
