from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', blank=True)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', blank=True)
    amount = models.FloatField(verbose_name="Сумма")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", blank=True)
    organization = models.CharField(max_length=200, verbose_name="Организация")
    description = models.CharField(max_length=200, verbose_name="Описание")

    class Meta:
        ordering = ('-created',)
