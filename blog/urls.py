from django.urls import path
from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetailView

app_name = BlogConfig.name

urlpatterns = [
    path("list/", ArticleListView.as_view(), name="article_list"),
    path("article_view/<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
]