from django.conf.urls import url
from django.contrib import admin

from quotes.views import QuoteList, AuthorQuoteList

urlpatterns = [
    url(r'^$', QuoteList.as_view(), name='quote-list'),
    url(r'^author/(?P<slug>[\w-]+)/$', AuthorQuoteList.as_view(), name='author-list'),
    url(r'^admin/', admin.site.urls),
]
