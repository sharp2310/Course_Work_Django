from django.contrib.auth.forms import UserCreationForm
from django import forms

from schedule.forms import MixinForms
from users.models import User, Company


class UsersRegisterForm(UserCreationForm):
    existing_company = forms.ModelChoiceField(
        queryset=Company.objects.all(), required=False, label="Существующая компания"
    )
    new_company = forms.CharField(
        max_length=150, required=False, label="Новая компания"
    )

    class Meta:
        model = User
        fields = ("email", "existing_company", "new_company", "password1", "password2")

    def clean(self):
        cleaned_data = super().clean()
        existing_company = cleaned_data.get("existing_company")
        new_company = cleaned_data.get("new_company")

        if not existing_company and not new_company:
            raise forms.ValidationError(
                "Необходимо выбрать существующую компанию или ввести новую."
            )

        if existing_company and new_company:
            raise forms.ValidationError(
                "Можно выбрать только одну опцию: либо существующую компанию, либо ввести новую."
            )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        existing_company = self.cleaned_data["existing_company"]
        new_company = self.cleaned_data["new_company"]

        if existing_company:
            user.user_company = existing_company
        elif new_company:
            company, created = Company.objects.get_or_create(company_name=new_company)
            user.user_company = company

        if commit:
            user.save()

        return user