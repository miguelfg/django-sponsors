# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^index/$', views.IndexView.as_view(), name='template-index'),
    url(r'^list/$', views.SponsorsList.as_view(), name='list-sponsors'),
)
