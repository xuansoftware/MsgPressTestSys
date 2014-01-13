# -*- coding: utf-8 -*-
'''
Created on 2013年9月30日

@author: andyxzhang
'''

import time

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from forms import *  # @UnusedWildImport
from models import *  # @UnusedWildImport
# from util.paths import *  # @UnusedWildImport


__all__ = ['HomeView',
           'CreateTaskView',
           'ReportView',
           'TaskListView',
           ]

class HomeView(ListView):
    u'''主界面'''

    template_name = 'base.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context
    
    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('new_task'))
    
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('task_list'))
    

class CreateTaskView(TemplateView):
    u'''新建任务上传界面'''
    
    template_name = 'home/create_new_task.html'
    
#     # 该方法不能删除，删除后会报ImproperlyConfigured错误
#     def get_queryset(self, *args, **kwargs):
#         qs = []
#         return qs

    def get_context_data(self, **kwargs):
        context = super(CreateTaskView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = ContactForm()
        return context
    
    def get(self, request, *args, **kwargs):
#         form = ContactForm()
        context = self.get_context_data()
        return self.render_to_response(context)
#         return self.render_to_response({'form':form})
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
        
        uploadTime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        task_id = int(uploadTime)
        print 'newTask:', task_id
        
        login_uid = 0
        task_uid=cd['task_uid']
        msg=cd['msg'] 
        type=cd['type']
        count=cd['count']
        
        print 'task_uid', task_uid
        print 'msg', msg
        print 'type', type
        print 'count', count
        
        
        TaskInfo.insert(task_id=task_id, login_uid=login_uid, task_uid=cd['task_uid'],
                         msg=cd['msg'], type=cd['type'], count=cd['count'], status=0)
        
        return HttpResponseRedirect(reverse('task_list'))
    

class ReportView(TemplateView):
    u'''报告展示页面'''
    
    template_name = 'home/report.html'
    
    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        return context
    
    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('home'))
    
    def get(self, request, *args, **kwargs):
        task_id = request.GET.get('task_id')
        task = ResultInfo.objects.get(task_id=task_id)
        host_url = 'http://' + request.get_host()
        path = '/static/data/' + task_id + '/' + task.url + '/index.html'
#         return HttpResponseRedirect(REPORT_DIR + task.url+'/index.html')
        return HttpResponseRedirect(host_url + path)


class TaskListView(TemplateView):
    u'''任务列表界面'''
    
    model = ResultInfo
    template_name = 'home/tasklist.html'
    
    def get_all_queryset(self):
        # 获取任务信息
        qs = TaskInfo.objects.all().order_by('-task_id')
        return qs

    def get_queryset(self):
        # 获取任务信息
#         qs = MemoryAnalyzeTaskInfo.objects.filter(task_id__range = (0, 2))
        # 使用中若延时过大就改为直接采取sql语句查询
        qs = TaskInfo.objects.order_by('-task_id')[0: 30]
        return qs
        
    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        getAll = kwargs['getAll']
        if getAll:
            context['tasks'] = self.get_all_queryset()
            context['isNotAll'] = False
        else:
            context['tasks'] = self.get_queryset()
            context['isNotAll'] = True
        return context
    
    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('home'))
    
    def get(self, request, *args, **kwargs):
        getAll = request.GET.get('getAll')
        context = self.get_context_data(getAll=getAll)
        return self.render_to_response(context)

