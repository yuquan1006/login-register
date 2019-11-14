from django.db import models

# Create your models here.


class User(models.Model):
    '''用户表：用户名/密码/邮箱地址/性别/创建时间'''

    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 50,unique=True)
    passWord = models.CharField(max_length= 128)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    createTime = models.DateTimeField("创建时间",auto_now_add=True)
    updateTime = models.DateTimeField("更新时间",auto_now=True)

    def __str__(self):
        '''使用__str__方法帮助人性化显示对象信息；'''
        return self.name

    class Meta:
        '''元数据里定义用户按创建时间的反序排列，也就是最近的最先显示'''
        db_table = 'user'  # 指定在数据库中，当前模型生成的数据表的表名。比如：
        verbose_name = '用户表'  # 用于设置模型对象的直观、人类可读的名称。可以用中文
        ordering = ["-createTime"]  # 用于指定该模型生成的所有对象的排序方式


