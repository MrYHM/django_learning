from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    '''用户学习的主题'''
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User)

    # 使用哪些属性来显示主题的信息
    # 返回存储在属性text中的字符串
    def __str__(self):
        return self.text

class Entry(models.Model):
    '''学到的有关某个主题的具体知识'''
    topic = models.ForeignKey(Topic)   # 将每个条目关联到特定的主题
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    # 存储用于管理模型的额外信息
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."
                                                                                                                                                                                                                                                                                                                                                                                   
