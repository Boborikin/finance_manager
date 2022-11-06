import django_filters
from django_filters import DateTimeFilter, NumberFilter

from .models import Transaction


class CustomTransactionFilter(django_filters.FilterSet):
    created = DateTimeFilter(field_name='created', lookup_expr='exact')
    created_gte = DateTimeFilter(field_name='created', lookup_expr='gte')
    created_lte = DateTimeFilter(field_name='created', lookup_expr='lte')
    created_gt = DateTimeFilter(field_name='created', lookup_expr='gt')
    created_lt = DateTimeFilter(field_name='created', lookup_expr='lt')

    amount = NumberFilter(field_name='amount', lookup_expr='exact')
    amount_gte = NumberFilter(field_name='amount', lookup_expr='gte')
    amount_lte = NumberFilter(field_name='amount', lookup_expr='lte')
    amount_gt = NumberFilter(field_name='amount', lookup_expr='gt')
    amount_lt = NumberFilter(field_name='amount', lookup_expr='lt')

    class Meta:
        model = Transaction
        fields = ('created', 'amount')
