from django.db import models


# Create your models here.
from django.utils import timezone


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, verbose_name='用户名')
    u_gender = ((0, '保密'), (1, '男'), (2, '女'))
    gender = models.IntegerField(default=0, choices=u_gender, null=True, verbose_name='性别')
    password = models.CharField(max_length=128, verbose_name='密码')
    phonenum = models.CharField(max_length=11, verbose_name='手机号码')
    email = models.EmailField(null=True, verbose_name='邮箱')

    fullname = models.CharField(max_length=100, verbose_name='真实姓名')
    cost = models.IntegerField(null=True, verbose_name='总花费')
    score = models.IntegerField(null=True, verbose_name='积分')

    def __main__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name_plural = '用户表'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户名')
    p_num = ((1, '1-2人'), (2, '3-4人'), (3, '5-8人'), (4, '8人以上'))
    person = models.IntegerField(verbose_name='用餐人数', default=1, choices=p_num)
    message = models.CharField(max_length=1000, verbose_name='内容')
    subject = models.CharField(max_length=100, verbose_name='主题')
    O_status = ((0, '等待处理'), (1, '预约成功'), (2, '取消订单'), (3, '拒绝订单'), (4, '已完成订单'))
    status = models.IntegerField(default=0, choices=O_status, verbose_name='订单状态')
    time = models.DateTimeField('预约用餐时间')
    send_time = models.DateTimeField('发送订单时间', default=timezone.now)
    last_time = models.DateTimeField('最后修改时间', auto_now=True)

    class Meta:
        db_table = 'order'
        verbose_name_plural = '预约表'


class Team(models.Model):

    name = models.CharField(max_length=100, )
    title = models.CharField(max_length=100, )
    content = models.CharField(max_length=10000, )
    images = models.FileField()

    class Meta:
        db_table = 'team'
        verbose_name_plural = 'TEAM'


class Menu(models.Model):
    name = models.CharField(max_length=100, )
    price = models.IntegerField(verbose_name='价格')
    title = models.CharField(max_length=100, )
    content = models.CharField(max_length=10000, )
    images = models.FileField()
    m_type = ((0, '臻选午餐'), (1, '浪漫晚餐'), (2, '水果甜品'), (3, '饮料咖啡'))
    m_class = models.IntegerField(default=0, choices=m_type, )
    create_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'menu'
        verbose_name_plural = '菜单'


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    name = models.CharField(max_length=100, )
    title = models.CharField(max_length=100, )
    content = models.CharField(max_length=10000, )
    images = models.FileField()
    images2 = models.FileField()
    images3 = models.FileField()
    images4 = models.FileField()
    create_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'blog'
        verbose_name_plural = '博客'




