from django import forms
from mail_messages.models import Message
from customers.forms import StyleFormMixin


class MessageForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания/редактирования сообщения"""

    class Meta:
        model = Message
        exclude = ("owner",)