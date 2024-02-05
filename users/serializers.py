from rest_framework import serializers
from users.models import User, Payments


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    date_joined = serializers.DateTimeField(format="%Y-%m-%d")
    history_payments = PaymentsSerializer(many=True, read_only=True, source='payments_set')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined', 'history_payments']

    def get_history_payments(self, objects):
        return objects.history_payments
