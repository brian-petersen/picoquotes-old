from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from .models import Quote, Author


class QuoteList(ListView):
    model = Quote
    template_name = 'quotes/quote_list.html'


class AuthorQuoteList(ListView):
    template_name = 'quotes/quote_list.html'

    def get_queryset(self):
        self.author = get_object_or_404(Author, slug=self.kwargs['slug'])
        return Quote.objects.filter(author=self.author)
