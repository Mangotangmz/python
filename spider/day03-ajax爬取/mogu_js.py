import pymysql
import requests
from lxml import etree
import json


# 取页面HTML
def get_one_page(url):
    # url = 'https://list.mogujie.com/search?callback=jQuery211014301867232186138_1540348924426&_version=8193&ratio=3%3A4&cKey=15&page=2&sort=pop&ad=0&fcid=10056642&action=jiadian&acm=3.mce.1_10_1hheg.110546.0.dc7J0r7mirDbg.pos_1-m_407824-sd_119-mf_15261_1047900-idx_0-mfs_22-dm1_5000&ptp=1._mf1_1239_15261.0.0.PmrAUvbX&_=1540348924430'
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        # print(text)
        return text
    return None


def get_all_pages():
    num = 1
    keys = ['tradeItemId', 'itemType', 'img', 'clientUrl', 'link', 'itemMarks', 'acm', 'price_taglist', 'title',
                 'cparam', 'orgPrice', 'hasSimilarity', 'lefttop_taglist', 'sale', 'cfav', 'price',
                 'leftbottom_taglist', 'similarityUrl']
    while True:
        url = 'https://list.mogujie.com/search?callback=jQuery211014301867232186138_1540348924426&_version=8193&ratio=3%3A4&cKey=15&page={}'.format(num)
        html = get_one_page(url)
        html_content = get_real_content(html)
        result = json.loads(html_content)
        # print(result)
        # 获取需要内容列表
        goods_lists = result['result']['wall']['docs']
        print(goods_lists)
        into_db(goods_lists,keys)
        print(result['status']['code'])
        num += 1
        print(num)
        if result['result']['wall']['isEnd'] == True:
            break


def get_real_content(html):
    if html and len(html) > 128:
        i = html.index('(')
        html1 = html[i + 1:]
        html1 = html1.replace(');', '')
        print(html1)
        return html1
    return None


def main():
    get_all_pages()


'''存商品信息到数据库'''


def into_db(goods_lists,keys):
    # 创建连接
    coon = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mogujie')

    # 创建游标
    cursor = coon.cursor()


    for item in goods_lists:
        list=[]
        value_list = []
        for i in keys:
            value = item.get(i)
            value_list.append(value)
        list.extend(keys)
        list.extend(value_list)
        value_tuple = tuple(list)
        print(len(keys))

        sql = """insert into goods(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")  """ % value_tuple
        try:
            cursor.execute(sql)
            coon.commit()
            print('写入成功')
        except:
            continue




    coon.close()


if __name__ == '__main__':
    main()
