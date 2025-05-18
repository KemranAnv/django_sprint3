"""Admin zone of blog."""

from django.contrib import admin
from .models import Post, Category, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """PostAdmin."""

    list_display = ('title', 'pub_date', 'author', 'location',
                    'is_published', 'created_at', 'category')
    list_editable = ('is_published', 'category')
    search_fields = ('title',)
    list_filter = ('category', 'is_published')
    list_display_links = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """CategoryAdmin."""

    list_display = ('title', 'created_at', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """LocationAdmin."""

    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)
    list_display_links = ('name',)
