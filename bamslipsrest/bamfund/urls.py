from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bamfund import views

urlpatterns = [
    url(r'^funds/$', views.fund_list),
    url(r'^funds/(?P<pk>[0-9]+)$', views.fund_detail),
    url(r'^fund_net/$', views.fund_net_list),
    url(r'^fund_net/(?P<pk>[0-9]+)$', views.fund_net_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
