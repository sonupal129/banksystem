from .imports import *
from .models import Account
# CODE Below

class AccountForm(forms.Form):
    account = forms.ModelChoiceField(queryset=Account.objects.all(), label="Select Account")

class TransactionForm(AccountForm):
    transaction_choice = {
        ("CR", "Deposit"),
        ("DR", "Withdraw")
    }

    amount = forms.DecimalField(max_digits=10, min_value=0)
    transaction_type = forms.ChoiceField(choices=transaction_choice)

    def clean(self): 
        data = super(TransactionForm, self).clean()       
        amount = data.get("amount")
        account = data["account"]
        transaction_type = data["transaction_type"]
        if transaction_type == "DR":
            balance = account.balanceEnquiry()
            if balance - amount < 0 and transaction_type == "DR":
                self.add_error("amount", "less amount")
        return data
    
class TransactionExportForm(AccountForm):
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), initial=datetime.now().date()-timedelta(days=60))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), initial=datetime.now().date())