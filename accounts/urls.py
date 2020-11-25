from .imports import *
from .views import *
from .api_views import *
from django.urls import include
from django.views.decorators.csrf import csrf_exempt
# CODE BELOW

apiUrlPatterns = [
    path ('banking/', BankingAPIView.as_view(), name="banking"),
    path ('banking/enquiry/balance/<int:account_number>/', BankingAPIView.as_view(), name="balance_enquiry"),
    path ('banking/export/transactions/', ExportAPIView.as_view(), name="tranaction_export"),
]


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('export/', TransactionExportView.as_view(), name="export"),
    path("api/v1/", include(apiUrlPatterns), name="api_urls")
]