from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from customers.forms import CustomerForm
from customers.models import Customer
from mailing.views import ManagerOrOwnerRequiredMixin, OwnerRequiredMixin


class CustomerListView(ListView):
    """Контроллер создания клиента сервиса"""
    model = Customer
    paginate_by = 15
    ordering = ['-id']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('mailing:access_error')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        if not self.request.user.is_manager:
            queryset = queryset.filter(owner=self.request.user.pk)
        return queryset


class CustomerCreateView(LoginRequiredMixin, CreateView):
    """Контроллер просмотра списка клиентов сервиса"""
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customers:customer_list')

    def form_valid(self, form):
        if form.is_valid():
            contact = form.save()
            contact.owner = self.request.user
            contact.save()

        return super().form_valid(form)


class CustomerDetailView(ManagerOrOwnerRequiredMixin, DetailView):
    """Контроллер просмотра отдельного клиента сервиса"""
    model = Customer


class CustomerUpdateView(OwnerRequiredMixin, UpdateView):
    """Контроллер редактирования клиента сервиса"""
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customers:customer_list')


class CustomerDeleteView(OwnerRequiredMixin, DeleteView):
    """Контроллер удаления клиента сервиса"""
    model = Customer
    success_url = reverse_lazy('customer:customer_list')