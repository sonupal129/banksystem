from .imports import *
from .forms import *
from .mixins import *
# Create your views here.


class HomeView(BasePermissionMixin, GroupRequiredMixins, FormView):
    http_method_names = ["get", "post"]
    template_name = "templates/home.html"
    group_required = ["customer", "manager"]
    
    def get_context_data(self, **kwargs):
        if "transaction_form" not in kwargs:
            kwargs["transaction_form"] = TransactionForm
        if "enquiry_form" not in kwargs:
            kwargs["enquiry_form"] = AccountForm
        return kwargs
    
    def post(self, request, **kwargs):
        if "transaction_form" in request.POST:
            form = TransactionForm(request.POST)
            if form.is_valid():
                amount = form.cleaned_data["amount"]
                account = form.cleaned_data["account"]
                transaction_type = form.cleaned_data["transaction_type"]
                if transaction_type == "CR":
                    account.depositMoney(amount)
                elif transaction_type == "DR":
                    account.withdrawMoney(amount)
                kwargs["balance"] = account.balanceEnquiry()
        elif "enquiry_form" in request.POST:
            form = AccountForm(request.POST)
            if form.is_valid():
                account = form.cleaned_data["account"]
                kwargs["balance"] = account.balanceEnquiry()
        return self.render_to_response(self.get_context_data(**kwargs))


class TransactionExportView(BasePermissionMixin, GroupRequiredMixins, FormView):
    http_method_names = ["get", "post"]
    template_name = "templates/export.html"
    form_class = TransactionExportForm
    group_required = ["manager"]


    def post(self, request, **kwargs):
        form = self.get_form()
        if form.is_valid():
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]
            account = form.cleaned_data["account"]
            kwargs["transactions"] = account.getTransactionData(start_date, end_date)
            kwargs["start_date"] = start_date
            kwargs["end_date"] = end_date
            kwargs["account"] = account
        return self.render_to_response(self.get_context_data(**kwargs))


    



    