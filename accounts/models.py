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
    account_number = models.PositiveIntegerField(default=generateRandomNumbers(10000000,99999999), editable=False)
    phone_number = PhoneNumberField(blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(Decimal('0.00'))])

    def __str__(self):
        return str(self.account_number)

    def depositMoney(self, amount:float=0):
        Transaction.objects.create(account=self, transaction_type="CR", amount=amount)
        self.balance += amount
        self.save()
        return self.balance

    def withdrawMoney(self, amount=0):
        Transaction.objects.create(account=self, transaction_type="DR", amount=amount)
        self.balance -= amount
        self.save()
        return self.balance

    def balanceEnquiry(self):
        return self.balance

    def getTransactionData(self, start_date=datetime.now().date() - timedelta(days=60), end_date=datetime.now().date()):
        transaction = self.transactions.filter(created_at__range=[start_date, end_date + timedelta(days=1)])
        return transaction

    def exportTrasactionData(self, start_date=datetime.now().date() - timedelta(days=60), end_date=datetime.now().date()):
        data = self.getTransactionData(start_date, end_date).values()
        df = pd.DataFrame(list(data))
        fileName = hashlib.sha256().hexdigest()[:10] + ".csv"
        filePath = "/".join([settings.MEDIA_ROOT, "exports", fileName])
        df.to_csv(filePath, encoding="utf-8")
        completePath = "/".join([settings.SITE_URL, "media/exports",fileName])
        return completePath


class Transaction(BaseModelClass):
    transaction_choice = {
        ("DR", "Debit"),
        ("CR", "Credit")
    }

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    transaction_number = models.PositiveIntegerField(default=generateRandomNumbers(10000000,99999999), editable=False)
    transaction_type = models.CharField(max_length=4, choices=transaction_choice, default=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return " | ".join([str(self.transaction_number), self.transaction_type])
