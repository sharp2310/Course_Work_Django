from django import forms
from customers.models import Customer


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CustomerForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Customer
        exclude = ('owner',)