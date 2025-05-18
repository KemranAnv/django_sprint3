from django.views.generic import ListView, DetailView
from datetime import date
from .models import Post, Category

from django.utils import timezone
# Добавил импорт
from django.shortcuts import render, get_object_or_404
from django.http import Http404


# Create your views here.
class IndexView(ListView):
    model = Post
    template_name ='blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        ).select_related(
            'category', 'location', 'author'
        ).order_by(
            '-pub_date'
        )[:5]


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(
            Post.objects.filter(
                is_published=True,
                pub_date__lte=timezone.now(),
                category__is_published=True
            ).select_related(
                'category', 'location', 'author'),
                pk=self.kwargs['pk']
        )


class CategoryPostView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(
            category__slug=self.kwargs['slug'],
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
        ).select_related(
            'category', 'location', 'author'
        ).order_by(
            '-pub_date'
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category.objects.filter(is_published=True),
            slug=self.kwargs['slug'])
        return context






# def index(request):
#     template = 'blog/index.html'
#     context = {
#         'posts': posts[::-1]
#     }
#     return render(request, template, context)


# Выполнение обязательных критериев
# def post_detail(request, id):
#     template = 'blog/detail.html'
#     post = next((post for post in posts if post['id'] == id), None)
#     if post is None:
#         raise Http404("Пост не найден")

#     context = {
#         'post': post
#     }

#     return render(request, template, context)


# def category_posts(request, category_slug):
#     template = 'blog/category.html'
#     filtered_posts = [post for post in posts
#                       if post['category'] == category_slug]
#     context = {
#         'category_slug': category_slug,
#         'posts': filtered_posts
#     }
#     return render(request, template, context)


# Deleted to work with DateBases
# posts = [
#     {
#         'id': 0,
#         'location': 'Остров отчаянья',
#         'date': '30 сентября 1659 года',
#         'category': 'travel',
#         'text': '''Наш корабль, застигнутый в открытом море
#                 страшным штормом, потерпел крушение.
#                 Весь экипаж, кроме меня, утонул; я же,
#                 несчастный Робинзон Крузо, был выброшен
#                 полумёртвым на берег этого проклятого острова,
#                 который назвал островом Отчаяния.''',
#     },
#     {
#         'id': 1,
#         'location': 'Остров отчаянья',
#         'date': '1 октября 1659 года',
#         'category': 'not-my-day',
#         'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
#                 с мели приливом и пригнало гораздо ближе к берегу.
#                 Это подало мне надежду, что, когда ветер стихнет,
#                 мне удастся добраться до корабля и запастись едой и
#                 другими необходимыми вещами. Я немного приободрился,
#                 хотя печаль о погибших товарищах не покидала меня.
#                 Мне всё думалось, что, останься мы на корабле, мы
#                 непременно спаслись бы. Теперь из его обломков мы могли бы
#                 построить баркас, на котором и выбрались бы из этого
#                 гиблого места.''',
#     },
#     {
#         'id': 2,
#         'location': 'Остров отчаянья',
#         'date': '25 октября 1659 года',
#         'category': 'not-my-day',
#         'text': '''Всю ночь и весь день шёл дождь и дул сильный
#                 порывистый ветер. 25 октября.  Корабль за ночь разбило
#                 в щепки; на том месте, где он стоял, торчат какие-то
#                 жалкие обломки,  да и те видны только во время отлива.
#                 Весь этот день я хлопотал  около вещей: укрывал и
#                 укутывал их, чтобы не испортились от дождя.''',
#     },
# ]