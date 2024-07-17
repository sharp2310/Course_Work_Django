from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from schedule.apps import ScheduleConfig
from schedule.services import toggle_activity
from schedule.views.client import (
    ClientsListView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
)
from schedule.views.home import HomeView
from schedule.views.newsletter import (
    NewsletterListView,
    NewsletterCreateView,
    NewsletterUpdateView,
    NewsletterDeleteView,
    NewsletterLDetailView,
)
from schedule.views.text_for_newsletter import (
    TextForNewsletterListView,
    TextForNewsletterCreateView,
    TextForNewsletterUpdateView,
    TextForNewsletterDeleteView,
)

app_name = ScheduleConfig.name

urlpatterns = [
    path("", cache_page(180)(HomeView.as_view()), name="home"),
    path("client_list/", ClientsListView.as_view(), name="client_list"),
    path("client_form/", ClientCreateView.as_view(), name="client_form"),
    path("<int:pk>/client_update", ClientUpdateView.as_view(), name="client_update"),
    path("<int:pk>/client_delete", ClientDeleteView.as_view(), name="client_delete"),
    path("newsletter_list/", NewsletterListView.as_view(), name="newsletter_list"),
    path(
        "newsletter_detail/<int:pk>",
        NewsletterLDetailView.as_view(),
        name="newsletter_detail",
    ),
    path("activity/<int:pk>", toggle_activity, name="toggle_activity"),
    path("newsletter_form/", NewsletterCreateView.as_view(), name="newsletter_form"),
    path(
        "<int:pk>/newsletter_update",
        NewsletterUpdateView.as_view(),
        name="newsletter_update",
    ),
    path(
        "<int:pk>/newsletter_delete",
        NewsletterDeleteView.as_view(),
        name="newsletter_delete",
    ),
    path(
        "textfornewsletter_list/",
        TextForNewsletterListView.as_view(),
        name="textfornewsletter_list",
    ),
    path(
        "textfornewsletter_form/",
        TextForNewsletterCreateView.as_view(),
        name="textfornewsletter_form",
    ),
    path(
        "<int:pk>/textfornewsletter_update",
        TextForNewsletterUpdateView.as_view(),
        name="textfornewsletter_update",
    ),
    path(
        "<int:pk>/textfornewsletter_delete",
        TextForNewsletterDeleteView.as_view(),
        name="textfornewsletter_delete",
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)