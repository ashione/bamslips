from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bamfund import views

urlpatterns = [
    url(r'^v1/funds/$', views.FundList.as_view()),
    url(r'^v1/funds/(?P<pk>[0-9]+)$', views.FundDetail.as_view()),
    url(r'^v1/fund_net/$', views.FundNetList.as_view()),
    url(r'^v1/fund_net/(?P<pk>[0-9]+)$', views.FundNetDetail.as_view()),
    url(r'^v1/fund_realtime/$', views.FundRealTimeNetList.as_view()),
    url(r'^v1/fund_realtime/(?P<pk>[0-9]+)$', views.FundRealTimeNetDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns.extend( [
    url(r'^index/$',views.index),
    url(r'^login/$',views.user_login),
    url(r'^logout/$',views.user_logout),
])
