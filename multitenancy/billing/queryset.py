from django.db import models
from django.db.models import Q


class InvoiceQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.all()
        lookups = (
            Q(subscription__product_type__name__icontains=query)
            | Q(id__exact=query)
            | Q(invoice_number__exact=query)
        )
        return self.filter(lookups)

    def filter_by_id(self, id=None):
        if id is None or id == "":
            return self.all()
        return self.filter(id__exact=id)

    def get_due_date(self, date=None):
        if date is None or date == "":
            return self.all()
        return self.filter(due_date__exact=date)

    def filter_date_range(self, start_date=None, end_date=None):
        if start_date is None and end_date is None:
            return self.all()
        return self.filter(date_created__range=(start_date, end_date))

    def get_status(self, status):
        if status is None or status == "":
            return self.all()
        return self.filter(status__exact=status)


class RefundQuerySet(models.QuerySet):
    def get_invoice(self, invoice_id=None):
        if invoice_id is None or invoice_id == "":
            return self.all()
        return self.filter(invoice_id__exact=invoice_id)


class CreditQuesrySet(models.QuerySet):
    def get_customer_credit(self, customer_id=None):
        if customer_id is None or customer_id == "":
            return self.all()
        return self.filter(customer_id__exact=customer_id)
