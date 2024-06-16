from django import forms

from customers.models import Customer
from mail_messages.models import Message
from mailing.models import Mailing
from customers.forms import StyleFormMixin


class MailingForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания/редактирования рассылки"""

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields["customers"].queryset = Customer.objects.filter(owner=user)
        self.fields['messages'].queryset = Message.objects.filter(owner=user)

    class Meta:
        model = Mailing
        exclude = ("owner",)
class MailingManagerForm(StyleFormMixin, forms.ModelForm):
    """Форма для менеджера для изменения статуса рассылки"""
    class Meta:
        model = Mailing
        fields = ("status",)