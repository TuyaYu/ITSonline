# -*- encoding:utf-8 -*-

from django import forms
import re
from operation.models import *

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']
    
    def clean_model(self):
        #手机号码合法验证
            mobile = self.cleaned_data['mobile']
            REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
            p = re.compile(REGEX_MOBILE)
            if p.match(mobile):
                return mobile
            else:
                raise forms.ValidationError(u'手机号码非法',code = 'mobile_invalid')

