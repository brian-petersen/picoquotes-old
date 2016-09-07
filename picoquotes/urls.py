from django.conf.urls import url
from django.contrib import admin

from quotes.views import QuoteList, FilterQuoteList

urlpatterns = [
    url(r'^$', QuoteList.as_view(), name='quote-list'),
    url(r'^filter/$', FilterQuoteList.as_view(), name='filter-list'),
    url(r'^admin/', admin.site.urls),
]
