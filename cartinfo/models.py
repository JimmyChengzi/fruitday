from django.db import models
from userinfo.models import *
from memberapp.models import *

ORDERSTATUS = (
    (1,'未支付'),
    (2,'已支付'),
    (3,'已取消'),
    (4,'已完成'),
)
# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo)
    goods = models.ForeignKey(Goods)
    ccount = models.IntegerField('数量')

    def __str__(self):
        #当前user对象去查找uname
        return self.user.uname

class Order(models.Model):
    user = models.ForeignKey(UserInfo)
    orderNo = models.CharField('订单号',max_length=50,null=False)
    cals = models.TextField('订单商品描述')
    orderStatus = models.IntegerField('订单状态',choices=ORDERSTATUS,default=1)

    def __str__(self):
        return self.orderNo

