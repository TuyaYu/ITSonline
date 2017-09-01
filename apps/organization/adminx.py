# -*- encoding:utf-8 -*-
import xadmin
from organization.models import *

class CityDictAdmin(object):
	list_display = ['name','desc','add_time']
	search_fields = ['name']
	list_filter = ['name','add_time']


class CourseOrgAdmin(object):
	list_display = ['name','desc','add_time']
	search_fields = ['name']
	list_filter = ['name','add_time']



class TeacherAdmin(object):
	list_display = ['org','name','work_company','point','add_time']
	search_fields = ['org','name','work_company','point']
	list_filter = ['org','name','work_company','point','add_time']




xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)