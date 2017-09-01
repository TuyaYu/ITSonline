# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 下午6:44
# @Author  : yuzeyu
# @Site    : 
# @File    : urls.py
# @Software: PyCharm


from courses.views import *
from django.conf.urls import url

urlpatterns = [
	url(r'^list/$',CourseListView.as_view(),name = 'course_list'),
	url(r'^detail/(?P<course_id>\d+)/$',CourseDetailView.as_view(),name = 'course_detail'),
	url(r'^video/(?P<course_id>\d+)/$',CourseVideoView.as_view(),name = 'course_video'),
	url(r'^comment/(?P<course_id>\d+)/$',CourseCommentView.as_view(),name = 'course_comment'),
	url(r'^add_comment/$',AddCommentView.as_view(),name = 'add_comment'),
 ]