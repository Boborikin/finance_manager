from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from .filters import CustomTransactionFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .services import get_balance, get_statistic


class BalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return JsonResponse(get_balance(request.user))


class StatisticView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return JsonResponse(get_statistic(request.user))


class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = CustomTransactionFilter
    serializer_class = TransactionSerializer
    ordering_fields = ('created', 'amount')
    search_fields = ('amount', 'description', 'category__title')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """При создании транзакции автором становится тот, кто создал"""
        if self.request.user.is_authenticated:
            instance = serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            instance = serializer.save(user=self.request.user)