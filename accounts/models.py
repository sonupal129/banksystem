from .imports import *
# Create your models here.

class BaseModelClass(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True
        ordering = ["created_at"]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email


class Account(BaseModelClass):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    account_number = models.PositiveIntegerField(default=generateRandomNumbers(1000000000,9999999999), editable=False)
    phone_number = PhoneNumberField(blank=True)
    balance = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return str(self.account_number)

    def depositMoney(self, money=0):
        pass

    def withdrawMoney(self, money=0):
        pass

    def balanceEnquiry(self):
        return 0


class Transaction(BaseModelClass):
    transaction_choice = {
        ("WD", "Withdraw"),
        ("DP", "Deposit")
    }

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_number = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=4, choices=transaction_choice, default=None)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return " | ".join([str(self.transaction_number), self.transaction_type])
