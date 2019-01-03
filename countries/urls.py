from django.conf.urls import url

from countries.api import FetchCountries

urlpatterns = [
    url(r'^fetch/countries$', FetchCountries.as_view(), name='countries'),
]