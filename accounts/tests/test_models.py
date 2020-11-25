from django.test import TestCase
from ..models import Account
from ..imports import *
# Create your tests here.

class AccountModelTestCase(TestCase):

    def setUp(self):
        self.account = Account.objects.first()

    def test_deposit_money_account(self):
        account = Account.objects.first()
        deposit = self.account.depositMoney(10.0)
        balance = account.balanceEnquiry()
        self.assertEqual(depost, balance)
