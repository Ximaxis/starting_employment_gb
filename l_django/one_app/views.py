from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Item
from .forms import ItemForm
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


def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        data = save_good_form(request, form, 'one_app/item_form.html')
    else:
        data = {
            'form_is_valid': False,
            'html_form': render_to_string('one_app/item_form.html', {'form': ItemForm()}, request=request)
        }

    return JsonResponse(data)


def save_good_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            items = Item.objects.all()
            data['html_item_list'] = render_to_string('one_app/include_table.html', {
                'object_list': items
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return data

