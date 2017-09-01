# -*- encoding:utf-8 -*-

#邮箱验证
from random import Random
from django.core.mail import send_mail


from users.models import EmailVerifyRecord
from ITSonline.settings import EMAIL_FROM



#生成随机字符串
def generate_random_str(randomlength=8):
	str = ''
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
	length = len(chars) - 1
	random = Random()
	for i in range(randomlength):
		str+=chars[random.randint(0,length)]
	return str



def send_register_email(email,send_type="register"):
	email_record = EmailVerifyRecord()
	code = generate_random_str(16)
	email_record.code = code
	email_record.email = email
	email_record.send_type = send_type
	email_record.save()

	email_title = ""
	email_boby = ""

	if send_type =="register":
		email_title  = "yumi在线网注册激活链接"
		email_boby = "请点击下面的链接激活你的帐号: http://127.0.0.1:8000/active/{0}".format(code)
		send_status =send_mail(email_title,email_boby,EMAIL_FROM,[email])
		if send_status:
			pass


def send_forget_email(email,send_type="forget"):
	email_record = EmailVerifyRecord()
	code = generate_random_str(16)
	email_record.code = code
	email_record.email = email
	email_record.send_type = send_type
	email_record.save()

	email_title = ""
	email_boby = ""
	
	if send_type == "forget":
		email_title  = "yumi在线网修改密码链接"
		email_boby = "请点击下面的链接修改你的帐号密码: http://127.0.0.1:8000/reset/{0}".format(code)
		send_status =send_mail(email_title,email_boby,EMAIL_FROM,[email])
		if send_status:
			pass
