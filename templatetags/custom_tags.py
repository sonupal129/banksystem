from django import template

# CODE Below

register = template.Library()

@register.simple_tag
def getTransactionExport(account_obj, start_date, end_date):
    return account_obj.exportTransactionData(start_date, end_date)
