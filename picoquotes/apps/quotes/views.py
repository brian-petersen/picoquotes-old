from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.models import User

from .models import Quote, Author


class QuoteList(ListView):
    model = Quote
    template_name = 'quotes/quote_list.html'


class FilterQuoteList(ListView):
    template_name = 'quotes/quote_list.html'

    def get_queryset(self):
        filters = {}
        for param in self.request.GET:
            value = self.request.GET[param]
            if param == 'author':
                filters['author'] = get_object_or_404(Author, slug=value)
            if param == 'user':
                filters['user'] = get_object_or_404(User, username=value)
            if param == 'query':
                filters['text__contains'] = value
        return Quote.objects.filter(**filters)
