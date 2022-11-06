from django.db.models import Sum, Max
from .models import Transaction
from django.utils import timezone


def get_balance(user):
    return {"balance": Transaction.objects.filter(user=user).aggregate(Sum("amount"))['amount__sum']}


def get_statistic(user):
    total_transactions = Transaction.objects.filter(user=user).count()
    total_max_amount = Transaction.objects.filter(user=user).aggregate(Max("amount"))['amount__max']
    transactions_today = Transaction.objects.filter(user=user, created__day=timezone.now().day,
                                                    created__month=timezone.now().month,
                                                    created__year=timezone.now().year).count()
    data = {"total_transactions": total_transactions,
            "transactions_today": transactions_today,
            "total_max_amount": total_max_amount}
    return data