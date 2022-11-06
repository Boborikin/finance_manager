from rest_framework import serializers
from .models import Transaction, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
        read_only_fields = ('user',)


class TransactionSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        data = super(TransactionSerializer, self).to_representation(value)
        data.update({"category": value.category.title})
        return data

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'category', 'organization', 'description', 'created']
        read_only_fields = ('created', 'user',)

