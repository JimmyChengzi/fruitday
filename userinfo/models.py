from django.db import models

# Create your models here.
#用户模块下
#用户表
class UserInfo(models.Model):
    uname = models.CharField('用户名',max_length=50,null=False)
    upwd = models.CharField('密码',max_length=200,null=False)
    uphone = models.CharField('手机',max_length=20,null=False)
    uemail = models.EmailField('Email',default='a@a.com')
    isAcitve = models.BooleanField('激活',default=True)

    def __str__(self):
        return self.uname

#地址表
class Address(models.Model):
    user = models.ForeignKey(UserInfo)
    address = models.CharField('地址',max_length=200,null=False)
    aname = models.CharField('收件人姓名',max_length=50,null=False)
    aphone = models.CharField('收件人手机',max_length=20,null=False)

    def __str__(self):
        return self.aname
