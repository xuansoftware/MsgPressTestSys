# -*- coding:utf-8 -*-

from django import forms

class ContactForm(forms.Form):
    task_uid = forms.CharField(20)
    msg = forms.CharField()
    type = forms.IntegerField()
    count = forms.IntegerField()
    
    