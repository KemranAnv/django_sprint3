"""Создание моделей."""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


def get_published_posts(queryset=None):
    """get_published_posts."""
    if queryset is None:
        queryset = Post.objects.all()
    return queryset.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).select_related('category', 'location', 'author')


class BaseModel(models.Model):
    """BaseModel."""

    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        """Meta."""

        abstract = True


class Category(BaseModel):
    """Тематическая категория."""

    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text=(
            'Идентификатор страницы для URL; '
            'разрешены символы латиницы, цифры, дефис и подчёркивание.'
        ),
    )

    class Meta:
        """Мета файлы для Category."""

        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """__str__."""
        return self.title


class Location(BaseModel):
    """Географическая метка."""

    name = models.CharField('Название места', max_length=256)

    class Meta:
        """Мета файлы для Location."""

        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        """__str__."""
        return self.name


class Post(BaseModel):
    """Публикация."""

    title = models.CharField('Заголовок', max_length=256, )
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем '
            '— можно делать отложенные публикации.'
        )
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        Location,
        verbose_name='Местоположение',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        """Мета файлы для Post."""

        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        """__str__."""
        return self.title
