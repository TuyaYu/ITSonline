# -*- encoding:utf-8 -*-
from __future__ import unicode_literals

from organization.models import *


# Create your models here.



class Course(models.Model):
	course_org = models.ForeignKey(CourseOrg, verbose_name=u'课程机构',null=True,blank=True)
	name = models.CharField(max_length=50, verbose_name=u"课程名")
	desc = models.CharField(max_length=300, verbose_name=u"课程描述")
	detail = models.TextField(max_length=500, verbose_name='课程详情')
	teacher = models.ForeignKey(Teacher,verbose_name='讲师名',null=True,blank=True)
	degreen = models.CharField(verbose_name=u'难度',choices=(('cj','初级'),('zj','中级'),('gj','高级')),max_length=10)
	learn_times = models.IntegerField(default=0,verbose_name='学习时长')
	students = models.IntegerField(default=0,verbose_name='学习人数')
	fav_num = models.IntegerField(default=0,verbose_name='收藏人数')
	image = models.ImageField(upload_to="courses/%Y/%m",verbose_name='封面图',max_length=100)
	click_num = models.IntegerField(default=0,verbose_name='点击数')
	category = models.CharField(max_length=20,verbose_name='课程类别',null=True,blank=True)
	tag = models.CharField(max_length=20,verbose_name='课程标签',default='')
	konw = models.CharField(max_length=100, verbose_name=u"课程须知",default='')
	tell = models.CharField(max_length=100,verbose_name=u"老师告述你",default='')
	add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')


	class Meta:
		verbose_name=' 课程'
		verbose_name_plural = verbose_name

	def get_zj_nums(self):
		return self.lesson_set.all().count()

	def get_learn_users(self):
		return self.usercourse_set.all()[:5]

	def get_learn_nums(self):
		return self.usercourse_set.all().count()

	def get_course_lesson(self):
		return self.lesson_set.all()


	def __unicode__(self):
		return self.name

class Lesson(models.Model):
	course = models.ForeignKey(Course,verbose_name='课程')
	name = models.CharField(max_length=100,verbose_name='章节名')
	add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

	class Meta:
		verbose_name=' 章节'
		verbose_name_plural = verbose_name

	def get_lesson_video(self):
		return self.video_set.all()


	def __unicode__(self):
		return self.name


class Video(models.Model):
	lesson = models.ForeignKey(Lesson,verbose_name='章节')
	name = models.CharField(max_length=100,verbose_name='视频名称')
	url = models.CharField(max_length=200,verbose_name='访问地址',default='')
	learn_times = models.IntegerField(default=0,verbose_name='学习时长')
	add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

	class Meta:
		verbose_name=' 视频'
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.name


class CourseResource(models.Model):
	course = models.ForeignKey(Course,verbose_name='课程')
	name = models.CharField(max_length=100,verbose_name='名称')
	download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name='资源文件',max_length=100)
	add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

	class Meta:
		verbose_name=' 资源'
		verbose_name_plural = verbose_name
