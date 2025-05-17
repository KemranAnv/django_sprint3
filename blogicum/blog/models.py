"""Создание моделей."""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model


# Create your models here.
class Post(models.Model):
    """Публикация."""

    pass


class Category(models.Model):
    """Тематическая категория."""

    pass


class Location(models.Model):
    """Географическая метка."""

    pass
