from datetime import datetime

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User, Payments


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    history_payments = PaymentsSerializer(many=True, read_only=True, source='payments_set')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'date_joined', 'history_payments']

    def get_history_payments(self, objects):
        return objects.history_payments


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        validated_data['date_joined'] = datetime.now(tz=datetime.utcnow().tzinfo)
        password = validated_data.pop('password', None)
        if password:
            validated_data['password'] = make_password(password)
        return super().create(validated_data)
