from .serializers import *
from .imports import *
from .models import Transaction, Account
# CODE BELOW
# class BaseAPIView(APIView):

class BaseAPIView(APIView):

    def default_response(self, data=None):
        default_response = {
            "success": True,
            "errors": []
        }
        return default_response

    def get_serializer(self, *args, **kwargs):
        if self.serializer_class:
            return self.serializer_class(*args, **kwargs)
        elif self.serializer_class == None:
            return None
        raise AttributeError("serializer_class Attribute not defined")

class BankingAPIView(BaseAPIView):
    http_method_names = ["post", "get"]
    
    def get_serializer(self, *args, **kwargs):
        
        serializers_data = {
            "GET": AccountSerializer,
            "POST": BankingSerializer
        }
        serializer_class = serializers_data.get(self.request.method)
        return serializer_class(*args, **kwargs)

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        default_response = self.default_response()
        if serializer.is_valid():
            data = serializer.data
            amount = Decimal(data["amount"])
            try:
                account = Account.objects.get(account_number=data["account_number"])
            except Exception as e:
                default_response["errors"].append({"account": str(e)})
                return Response(default_response, 404)
            if data["transaction_type"] == "CR":
                account.depositMoney(amount)
            elif data["transaction_type"] == "DR":
                account.withdrawMoney(amount)
            default_response["balance"] = account.balanceEnquiry()
            return Response(default_response, 201)
        return Response(serializer.errors, 200)

    def get(self, request, account_number, **kwargs):
        default_response = self.default_response()
        try:
            account = Account.objects.get(account_number=account_number)
        except Exception as e:
            default_response["errors"].append({"account": str(e)})
            return Response(default_response, 404)
        serializer = self.get_serializer(account)
        return Response(serializer.data, 200)


class ExportAPIView(BaseAPIView):
    http_method_names = ["post"]
    serializer_class = TransactionExportSerializer
    

    def post(self, request, **kwargs):
        default_response = self.default_response()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            try:
                account = Account.objects.get(account_number=data["account_number"])
            except Exception as e:
                default_response["errors"].append({"account": str(e)})
                return Response(default_response, 404)
            start_date = datetime.strptime(data["start_date"], "%Y-%m-%d").date()
            end_date = datetime.strptime(data["end_date"], "%Y-%m-%d").date()
            filePath = account.exportTrasactionData(start_date, end_date)
            default_response["exportPath"] = filePath
            return Response(default_response, 200)
        return Response(serializer.errors, 404)
        


