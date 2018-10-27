import requests
import pymysql
from bs4 import BeautifulSoup


# 取页面HTML
def get_one_page(url):
    # url = 'http://www.dianping.com/chengdu/ch10/g110'
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None


def get_all_page():
    all_shop = []
    for i in range(2, 4):
        url = 'http://www.dianping.com/chengdu/ch10/g110p' + str(
            i) + '?aid=93195650%2C68215270%2C22353218%2C98432390%2C107724883&cpt=93195650%2C68215270%2C22353218%2C98432390%2C107724883&tc=3'
        html = get_one_page(url)
        all_shop.append(parse_soup(html))
    return all_shop


def parse_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    # print(soup.title.string)
    # print(soup.head)

    #     获取节点名字
    #     print(soup.title.name)
    names = soup.select('.txt .tit a h4')
    # for item in names:
    #     print(item.string)
    prices = soup.select('.comment a b')
    # for item in prices:
    #     print(item)
    images = soup.select('.pic a img')
    # for item in images:
    #     print(item['data-src'])

    # 获取节点属性
    # 把一页的店铺信息存储在列表中
    items = []
    for i in range(len(names)):
        item = {}
        item['name'] = names[i].string
        item['price'] = prices[i].string
        item['image'] = images[i]['src']
        items.append(item)
    return items

    # print(len(names))
    # print(len(images))
    # print(parse)


'''把数据存入数据库中'''


def update_db(shops):
    # 创建连接
    coon = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='dazong')

    # 创建游标
    cursor = coon.cursor()

    # 建表
    # 关闭数据库连接

    #
    #
    # # 插入数据
    for item in shops:
        sql = """insert into shop(name,price,image) value (%s,%s,%s)"""
        try:
            cursor.execute(sql, item['name'], item['price'], item['image'])
            coon.commit()
        except:
            coon.rollback()
    coon.close()


def main():
    # shops = get_all_page()
    # update_db(shops)
    url= 'https://www.koubei.com/'
    get_one_page(url)
    # print(html)


if __name__ == '__main__':
    main()
