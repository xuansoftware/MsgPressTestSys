# -*- coding: utf-8 -*-
'''
Created on 2013年9月30日

@author: andyxzhang
'''
#from Magnifier import settings

from django.db import models

__all__ = ['ResultInfo',
           'TaskInfo',
           ]
        
class ModelEx(models.Model):
    class Meta:
        abstract = True
    
    '''补充的get方法内对类型进行了判断；而django本身没有insert方法'''
        
    @classmethod
    def get(cls, *args, **kwargs):
        if args and 'id' not in kwargs:
            pk = args[0]
            if isinstance(pk, basestring) and pk.isdigit():
                pk = int(pk)
            if isinstance(pk, (int, long)):
                kwargs['id'] = pk
        try:
            obj = cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            return None
        return obj

    @classmethod
    def insert(cls, **kwargs):
        obj = cls()
        obj.update(**kwargs)
        return obj

    @classmethod
    def insert_if_not_exists(cls, **kwargs):
        obj = cls.get(**kwargs) or cls.insert(**kwargs)
        return obj

    def update(self, **kwargs):
        for field in kwargs:
            setattr(self, field, kwargs[field])
        self.save()

class ResultInfo(ModelEx):
    '''分析结果'''
    
    class Meta:
        db_table = u'result_info'
        
    task_id = models.BigIntegerField(default=0)
    url = models.CharField(max_length=500, blank=True)
    
    
class TaskInfo(ModelEx):
    '''任务'''
    
    class Meta:
        db_table = u'task_info'
        
    '''login_uid是当前登录到系统的用户
        task_uid是消息要发送到的用户
        status是标记当前任务执行状态
        type是任务类型'''
    task_id = models.BigIntegerField(default=0)
    login_uid = models.CharField(max_length=20, blank=True)
    task_uid = models.CharField(max_length=20)
    msg = models.CharField(max_length=500, blank=True)
    type = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
