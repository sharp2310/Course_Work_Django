from django.contrib import admin

from users.models import User, Company


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "user_company", "is_active", "avatar")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "company_name",
    )