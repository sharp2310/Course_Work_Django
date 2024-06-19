from django import forms
from mailing.models import Mailing
from customers.forms import StyleFormMixin


class MailingForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания/редактирования рассылки"""

    class Meta:
        model = Mailing
        exclude = ('owner',)


class MailingManagerForm(StyleFormMixin, forms.ModelForm):
    """Форма для менеджера для изменения статуса рассылки """

    class Meta:
        model = Mailing
        fields = ('status', )