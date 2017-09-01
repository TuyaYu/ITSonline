# -*- encoding:utf-8 -*-
from courses.models import *
import xadmin


class CourseAdmin(object):
	list_display = ['name','desc','detail','degreen','learn_times','students','fav_num','image','click_num','add_time']
	search_fields = ['name','desc','detail','degreen','learn_times','students','fav_num','image','click_num']
	list_filter = ['name','degreen','learn_times','students','fav_num','click_num','add_time']


class LessonAdmin(object):
	list_display = ['course','name','add_time']
	search_fields = ['course','name']
	list_filter = ['course__name','name','add_time']


class VideoAdmin(object):
	list_display = ['lesson','name','add_time']
	search_fields = ['lesson','name']
	list_filter = ['lesson','name','add_time']


class CourseResourceAdmin(object):
	list_display = ['course','name','add_time']
	search_fields = ['course','name']
	list_filter = ['course','name','add_time']


xadmin.site.register(CourseResource,CourseResourceAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Course,CourseAdmin)