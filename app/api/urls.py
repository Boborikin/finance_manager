from .views import TransactionViewSet, CategoryViewSet, BalanceView, StatisticView
from rest_framework import routers
from django.urls import include, path


router = routers.DefaultRouter()
router.register("transactions", TransactionViewSet, basename="transactions")
router.register("categories", CategoryViewSet, basename="categories")


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/balance/", BalanceView.as_view()),
    path("v1/statistic/", StatisticView.as_view()),
]