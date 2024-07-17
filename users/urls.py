from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from config import settings
from users.apps import UserConfig
from users.form import UsersRegisterForm

from users.services import email_verification, toggle_activity
from users.views import UserCreateView, PasswortResetView, UserListView, UserDetailView

app_name = UserConfig.name


urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", UserCreateView.as_view(), name="registration"),
    path(
        "passwort_reset_view/",
        PasswortResetView.as_view(form_class=UsersRegisterForm),
        name="passwort_reset",
    ),
    path(
        "confirm-register/<str:token>/",
        email_verification,
        name="confirm-register",
    ),
    path("user_list/", UserListView.as_view(), name="user_list"),
    path("user_detail/<int:pk>", UserDetailView.as_view(), name="user_detail"),
    path("activity/<int:pk>", toggle_activity, name="activity"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)