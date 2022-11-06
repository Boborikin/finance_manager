from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Category


@receiver(post_save, sender=User)
def create_categories(sender, instance, created, **kwargs):
    """Добавление стандартных категорий для пользователя."""
    default_categories = []
    categories = ["Забота о себе", "Зарплата",
                  "Здоровье и фитнес", "Кафе и рестораны", "Машина",
                  "Образование", "Отдых и развлечения",
                  "Платежи, комиссии", "Покупки: одежда, техника", "Продукты", "Проезд"
                  ]
    for category in categories:
        default_categories.append(Category(title=category, user=instance))
    if created:
        Category.objects.bulk_create(default_categories)
