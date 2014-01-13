# -*- coding: utf-8 -*-
'''
Created on 2013年12月31日

@author: andyxzhang
'''

from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
#     (r'^$', views.uploaddata),
    url(r'^$', HomeView.as_view(), name = 'home'),
#     url(r'^$', TaskListView.as_view()),
    url(r'^new_task/$', CreateTaskView.as_view(), name = 'new_task'),
    url(r'^task_list/$', TaskListView.as_view(), name = 'task_list'),
    url(r'^task_list/report$', ReportView.as_view(), name = 'report'),
)