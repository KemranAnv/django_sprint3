"""View function of app blog."""

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Post, Category, get_published_posts


class IndexView(ListView):
    """Homepage model."""

    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """get_queryset."""
        return get_published_posts().order_by('pub_date')[:5]


class PostDetailView(DetailView):
    """PostDetail model."""

    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self):
        """get_object."""
        return get_object_or_404(
            get_published_posts(),
            pk=self.kwargs['pk']
        )


class CategoryPostView(ListView):
    """Category Post model."""

    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """get_queryset."""
        category = get_object_or_404(
            Category, slug=self.kwargs['slug'], is_published=True
        )
        return get_published_posts(category.posts.all())

    def get_context_data(self, **kwargs):
        """get_context_data."""
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category.objects.filter(is_published=True),
            slug=self.kwargs['slug'])
        return context
