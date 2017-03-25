from django.conf.urls import url
from django.contrib import admin

from quotes.views import (QuoteList, SearchQuoteList, AuthorQuoteList,
                          random_quote)

urlpatterns = [
    url(r'^$', QuoteList.as_view(), name='quote-list'),
    url(r'^search/$', SearchQuoteList.as_view(), name='search'),
    url(r'^author/(?P<slug>.+)/$', AuthorQuoteList.as_view(), name='author-list'),
    url(r'^random/$', random_quote, name='random-quote'),
    url(r'^admin/', admin.site.urls),
]
