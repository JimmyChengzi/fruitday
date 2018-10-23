from django.shortcuts import render, get_object_or_404
from memberapp.models import GoodsType
import random


# Create your views here.

#首页
def index(request):
    #把GOOD类后面的/去掉,没有特殊作用,为了复习切片
    good_id = request.GET.get('good')[:-1]
    #找分类标题为新鲜水果的所有商品
    good_type = get_object_or_404(GoodsType,title='新鲜水果')
    #反向查询商品信息,all()获取全部该标题的商品信息,转换为list格式,随机展示4个
    f_goods = random.sample(list(good_type.goods_set.all()),4)