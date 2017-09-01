# -*- encoding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger

from operation.models import *
# Create your views here.
from courses.models import *
from utils.mixin_utils import *


class CourseListView(View):
	def get(self,request):
		all_courses = Course.objects.all()



		#对课程机构进行分页
		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1

		p = Paginator(all_courses, 5, request=request)

		courses = p.page(page)


		return render(request, 'course-list.html', {
			'all_courses':courses,
			})


class CourseDetailView(View):
	def get(self,request,course_id):
		course = Course.objects.get(id=int(course_id))
		course.click_num += 1
		course.save()

		has_fav_course = False
		has_fav_org = False

		if request.user.is_authenticated():
			if UserFavorite.objects.filter(user = request.user,fav_id = course.id,fav_type = 1):
				has_fav_course = True
			if UserFavorite.objects.filter(user = request.user,fav_id = course.course_org.id,fav_type = 2):
				has_fav_org = True

		tag = course.tag
		if tag:
			relate_course = Course.objects.filter(tag=tag)[:1]
		else:
			relate_course = []
		return render(request, 'course-detail.html', {
			'course':course,
			'relate_course':relate_course ,
			'has_fav_course':has_fav_course,
			'has_fav_org':has_fav_org

			})


class CourseVideoView(LoginRequiredMixin,View):
	def get(self,request,course_id):
		course = Course.objects.get(id = int(course_id))

		user_cousers = UserCourse.objects.filter(course = course)
		user_ids = [user_couser.user.id for user_couser in user_cousers]
		all_user_courses = UserCourse.objects.filter(user_id__in = user_ids)
		course_ids = [user_couser.course.id for user_couser in user_cousers]
		relate_courses = Course.objects.filter(id__in = course_ids).order_by("-click_num")[:5]

		all_resource = CourseResource.objects.filter(course = course)
		return render(request, 'course-video.html', {
			'course':course,
			'course_resource':all_resource,
			'relate_courses':relate_courses
			})




class CourseCommentView(LoginRequiredMixin,View):
	def get(self,request,course_id):
		course = Course.objects.get(id = int(course_id))
		all_resource = CourseResource.objects.filter(course = course)
		all_comment = CourseComments.objects.all()
		return render(request, 'course-comment.html', {
			'course':course,
			'course_resource':all_resource,
			'course_comment':all_comment
			})



class AddCommentView(View):
	def post(self,request):
		if not request.user.is_authenticated():
			return HttpResponse('{"status":"fail","msg":"用户未登录"}',content_type = 'application/json')

		course_id = request.POST.get("course_id",0)
		comments = request.POST.get("comments",0)
		if course_id > 0 and comments:
			course_comments = CourseComments()
			course = Course.objects.get(id = int(course_id))
			course_comments.course = course
			course_comments.comments = comments
			course_comments.user = request.user
			course_comments.save()
			return HttpResponse('{"status":"success","msg":"评论成功"}',content_type = 'application/json')
		else :
			return HttpResponse('{"status":"fail","msg":"评论失败"}',content_type = 'application/json')