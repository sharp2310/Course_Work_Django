from django.views.generic import ListView, DetailView
from blog.models import Article


class ArticleListView(ListView):
    """Контроллер просмотра списка статей"""

    model = Article
    paginate_by = 6


class ArticleDetailView(DetailView):
    """Контроллер просмотра деталей статьи"""

    model = Article

    def get_object(self, queryset=None):
        article = super().get_object(queryset)
        article.views_count += 1
        article.save()
        return article