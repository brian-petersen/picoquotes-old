from random import randint

from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Quote, Author


class QuoteList(ListView):
    model = Quote
    template_name = 'quotes/list.html'


class SearchQuoteList(ListView):
    template_name = 'quotes/list.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Quote.objects.filter(
            Q(text__icontains=query) |
            Q(author__name__icontains=query)
        )


class AuthorQuoteList(ListView):
    template_name = 'quotes/list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Quote.objects.filter(
            author=get_object_or_404(Author, slug=slug))


def random_quote(request):
    count = Quote.objects.count()
    index = randint(1, count)
    quote = Quote.objects.get(pk=index)
    return render(request, 'quotes/detail.html', {'object':quote})
