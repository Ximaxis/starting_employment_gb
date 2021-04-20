from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Item
from django.urls import reverse_lazy
# Create your views here.


class Index(ListView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Список товаров"
        return context


class CreateItem(CreateView):
    model = Item
    success_url = reverse_lazy("one:index")
    fields = ['title', 'price', 'vendor', ]

