from .imports import *
from .views import *
# CODE BELOW

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('export/', TransactionExportView.as_view(), name="export"),
]