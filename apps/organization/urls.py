# -*- encoding:utf-8 -*-

from django.conf.urls import url,include
from organization.views import *

urlpatterns = [
	url(r'^list/$',OrgListView.as_view(),name = 'org_list'),
	url(r'^add_ask/$',UserAskView.as_view(),name = 'add_ask'),
	url(r'^course/(?P<org_id>\d+)/$',OrgCourseView.as_view(),name = 'org_course'),
	url(r'^desc/(?P<org_id>\d+)/$',OrgDescView.as_view(),name = 'org_desc'),
	url(r'^home/(?P<org_id>\d+)/$',OrgHomeView.as_view(),name = 'org_home'),
	url(r'^teacher/(?P<org_id>\d+)/$',OrgTeacherView.as_view(),name = 'org_teacher'),
	#机构收藏
	url(r'^add_fav/$',AddFavView.as_view(),name = 'add_fav')

]