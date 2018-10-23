from django.db import models

# Create your models here.
SEX = (
    (1,'男'),
    (2,'女'),
)
#商品分类表
class GoodsType(models.Model):
    title = models.CharField('分类名称',max_length=50,null=False)
    picture = models.ImageField('图片',upload_to='static/image/good_type')
    desc = models.TextField('描述')
    isDelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return self.title

#商品表
class Goods(models.Model):
    title = models.CharField('商品名称',max_length=50,null=False)
    price = models.DecimalField('价格',max_digits=8,decimal_places=2)
    desc = models.TextField('描述')
    picture = models.ImageField('图片',upload_to='static/image/goods')
    isActive = models.BooleanField('是否上架',default=True)
    type = models.ForeignKey(GoodsType)
    sex = models.IntegerField('性别',choices=SEX,default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/detail/?good={}/'.format(self.id)

    #判断前端页面显示男或者女
    def get_sex(self):
        if self.sex == 1:
            return '男'
        else:
            return '女'
