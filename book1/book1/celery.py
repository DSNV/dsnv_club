from __future__ import absolute_import #绝对路径导⼊
from celery import Celery
from django.conf import settings
import os
#设置系统的环境配置⽤的是Django的
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book1.settings")
#实例化celery
app = Celery('mycelery')
app.conf.timezone = "Asia/Shanghai"
#指定celery的配置来源 ⽤的是项⽬的配置⽂件settings.py
app.config_from_object("django.conf:settings")
#让celery ⾃动去发现我们的任务（task）
app.autodiscover_tasks() #你需要在app⽬录下 新建⼀个叫tasks.py（⼀定不要写错）⽂件