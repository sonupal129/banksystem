from .models import Account, Transaction, UserProfile
from .imports import *
# CODE BLEOW

class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="user.email")
    class Meta:
        model = UserProfile
        fields = ["phone", "is_active", "email"]


class AccountSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = Account
        fields = ["account_number", "phone_number", "balance", "user"]


class BankingSerializer(serializers.Serializer):
    transaction_choice = {
        ("CR", "Deposit"),
        ("DR", "Withdraw")
    }
    account_number = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = serializers.ChoiceField(choices=transaction_choice, allow_blank=False)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["account", "transaction_type", "amount", "created_at"]

class TransactionExportSerializer(serializers.Serializer):
    account_number = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()