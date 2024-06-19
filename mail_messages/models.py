from django.db import models

NULLABLE = {"blank": True, "null": True}


class Message(models.Model):
    message_subject = models.CharField(max_length=100, verbose_name="Тема письма")
    text = models.TextField(verbose_name="Текст письма")

    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, **NULLABLE, related_name='messages')

    def __str__(self):
        return self.message_subject

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"