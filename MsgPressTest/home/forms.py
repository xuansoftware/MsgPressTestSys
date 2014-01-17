# -*- coding:utf-8 -*-

from django import forms

class ContactForm(forms.Form):
    CHOICE=(('1','C2C'),('2','讨论组'),('3','群消息'))
    
    task_uid = forms.CharField(12)
    msg = forms.CharField(100)
    type = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICE)
    count = forms.IntegerField()
    
#     def clean_task_uid(self):
#         task_uid = self.cleaned_data['task_uid']
#         num_uid = len(task_uid.split())
#         if num_uid > 8:
#             raise forms.ValidationError(u"目标用户ID长度过长")
#         return task_uid
    
#     def clean_msg(self):
#         msg = forms.CharField
    