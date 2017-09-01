# -*- encoding:utf-8 -*-
import xadmin

from apps.users.models import *
from xadmin import views
#所有参数都为固定写法


#主题修改
class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True


#全局设置
class GlobalSettings(object):
	site_title = "yumi在线后台管理系统"
	site_footer = "yumi online"
	menu_style = 'accordion'       # 收起目录


class EmailVerifyRecordAdmin(object):
	list_display = ['code','email','send_type','send_time']
	search_fields = ['code','email','send_type']
	list_filter = ['code','email','send_type','send_time']


class  BannerAdmin(object):
	list_display = ['title','image','url','index','add_time']    #显示列表
	search_fields = ['title','image','url','index']        #增加搜索功能
	list_filter = ['title','image','url','index','add_time']   #增加搜索功能


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
