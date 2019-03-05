from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from .models import StoreItem
from .filters import StoreItemFilter


def home(request):
    items = StoreItem.objects.all()
    context = {
        'items': items
    }
    return render(request, 'webstore/home.html', context)


class StoreItemListView(ListView):
    model = StoreItem
    template_name = 'webstore/home.html'  # <app>/<model>_<viewtype>.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = StoreItemFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class StoreItemDetailView(DetailView):
    model = StoreItem
