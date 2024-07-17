from random import shuffle

from django.urls import reverse_lazy
from django.views.generic import ListView

from blog.models import Blog
from schedule.models import Newsletter, DONE, IN_WORK
from schedule.services import get_cached_blog


class HomeView(ListView):
    model = Newsletter
    template_name = "schedule/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = self.get_queryset()
        newsletters = queryset.filter()

        newsletters_done_count = newsletters.filter(status_of_newsletter=DONE).count()
        newsletters_active = newsletters.filter(status_of_newsletter=IN_WORK).count()
        unique_clients = newsletters.values("clients").distinct().count()

        context["newsletters_done_count"] = newsletters_done_count
        context["newsletters_active"] = newsletters_active
        context["unique_clients"] = unique_clients

        context["blogs_list"] = get_cached_blog(self.request)

        return context