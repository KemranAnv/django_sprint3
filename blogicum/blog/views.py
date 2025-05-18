"""View function of app blog."""

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Post, Category


class IndexView(ListView):
    """Homepage model."""

    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """get_queryset."""
        return Post.objects.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        ).select_related(
            'category', 'location', 'author'
        ).order_by(
            'pub_date'
        )[:5]


class PostDetailView(DetailView):
    """PostDetail model."""

    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self):
        """get_object."""
        return get_object_or_404(
            Post.objects.filter(
                is_published=True,
                pub_date__lte=timezone.now(),
                category__is_published=True
            ).select_related(
                'category', 'location', 'author'
            ), pk=self.kwargs['pk']
        )


class CategoryPostView(ListView):
    """Category Post model."""

    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """get_queryset."""
        return Post.objects.filter(
            category__slug=self.kwargs['slug'],
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
        ).select_related(
            'category', 'location', 'author'
        ).order_by(
            'pub_date'
        )

    def get_context_data(self, **kwargs):
        """get_context_data."""
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category.objects.filter(is_published=True),
            slug=self.kwargs['slug'])
        return context
