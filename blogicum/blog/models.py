"""Создание моделей."""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model


# Create your models here.
class Category(models.Model):
    """Тематическая категория."""

    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField()


class Location(models.Model):
    """Географическая метка."""

    name = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    """Публикация."""

    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
