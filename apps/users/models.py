from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 自定义user 继承AbstractUser
class UserProfile (AbstractUser):
    nick_name = models.CharField (max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField (verbose_name="生日", null=True, blank=True)
    # 单选 choice('数据库存储名称',form显示的名称)
    gender = models.CharField (choices=(("male", "男"), ("female", "女")), default="female", max_length=10)
    address = models.CharField (max_length=100, default="")
    mobile = models.CharField (max_length=11, null=True, blank=True)
    #上传目录
    image = models.ImageField (upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    #个性化设置
    class Meta:
        # admin中数据表显示名称
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
    #admin中list显示的名称
    def __unicode__(self):
        return self.username


class EmailVerifyRecord (models.Model):
    code = models.CharField (max_length=20, verbose_name="验证码")
    email = models.EmailField (max_length=50, verbose_name="邮箱")
    send_type = models.CharField (choices=(("register", "注册"), ("forget", "找回密码")), max_length=10)
    send_time = models.DateTimeField (default=datetime.now)
    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


class Banner (models.Model):
    title = models.CharField (max_length=100, verbose_name="标题")
    image = models.ImageField (upload_to="banner/%Y/%m", verbose_name="轮播图", max_length=100)
    url = models.URLField (max_length=200, verbose_name="访问地址")
    index = models.IntegerField (default=100, verbose_name="顺序")
    add_time = models.DateTimeField (default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
