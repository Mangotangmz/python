

from django.shortcuts import render

from goods.models import Goods, GoodsCategory


def index(request):
    if request.method == 'GET':
        """
        想要的数据类型
        {'goods_1': [goods object, goods object, goods object, goods object],
         'goods_2': [goods object, goods object, goods object, goods object],
         'goods_3': [goods object, goods object, goods object, goods object],
         'goods_4': [goods object, goods object, goods object, goods object],
         'goods_5': [goods object, goods object, goods object, goods object],
         'goods_6': [goods object, goods object, goods object, goods object]}
        """
        # 获取所有的商品
        category_types = GoodsCategory.CATEGORY_TYPE
        #获取商品，按照id降序排列
        goods = Goods.objects.all().order_by('-id')
        # 循环商品分类，并组装结果
        data_all = {}
        for type in category_types:
            data = []
            count = 0
            for good in goods:
                # 计数count，大于5则不添加数据
                if count < 4:
                    if type[0] == good.category.category_type:
                        data.append(good)
                        count += 1
            data_all['goods_' + str(type[0])] = data
        return render(request, 'index.html', {'data_all': data_all, 'category_types': category_types})


