from django.db import models

NULLABLE = {"blank": True, "null": True}


class Article(models.Model):
    """Класс Статья"""

    title = models.CharField(max_length=50, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текст")
    preview = models.ImageField(
        upload_to="articles/", **NULLABLE, verbose_name="Превью"
    )
    date = models.DateField(verbose_name="дата публикации")
    views_count = models.PositiveIntegerField(default=0, verbose_name="просмотры")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"