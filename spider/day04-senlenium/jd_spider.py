import time

import document as document
import pymysql
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree

chrome_options = webdriver.ChromeOptions()

browser = webdriver.Chrome(chrome_options=chrome_options)

'''无头浏览器'''
# browser=webdriver.phantomJS()


browser.set_window_size(1200, 800)
wait = WebDriverWait(browser, 5)

KEYWORD = '维生素'

#
# def get_tao_page():
#     url = 'https://www.taobao.com/?spm=a230r.1.1581860521.1.780e1b1eHJeGWd'
#     browser.get(url)
#
#     search = wait.until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '.search-combobox-input')))
#     search.clear()
#     search.send_keys('ysl')
#
#     submit = wait.until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.search-button button.btn-search')))
#     submit.click()

    # input = wait.until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_password_1')))
    # input.clear()
    # input.send_keys('tmz.19951026')
    # time.sleep(10)
    # submit = wait.until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_SubmitStatic')))
    # submit.click()
    # if page > 1:
    #     try:
    #         input = wait.until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage span  input.input-txt')))
    #
    #         submit = wait.until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage span.p-num a.pn-next')))
    #         input.clear()
    #         input.send_keys(page)
    #         submit.click()
    #     except:
    #         print()
    #
    # page_source = browser.page_source


def get_page(page):
    print(page)
    if page == 1:
        url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8' % KEYWORD
        browser.get(url)
    #
    if page > 1:

        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage span  input.input-txt')))

        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage span.p-num a.pn-next')))
        input.clear()
        input.send_keys(page)
        submit.click()

    for i in range(6):
        str_js = 'var step = document.body.scrollHeight / 6; window.scrollTo(0, step * %d)' % (i + 1)
        browser.execute_script(str_js)
        time.sleep(5)

    page_source = browser.page_source
    return page_source


def parse_page(page_source):
    """解析页面"""
    etree_html = etree.HTML(page_source)
    # 拿到所有的li标签
    products = etree_html.xpath('//div[@id="J_goodsList"]/ul[contains(@class, "gl-warp")]/li[@class="gl-item"]')
    # print(len(products))
    goods_list =[]
    # 每页的数据用一个列表装起来
    print(len(products))

    for product in products:
        goods = {}
        if product.xpath('.//div[contains(@class, "p-name p-name-type-2")]/a/em/text()'):
            goods['name'] = product.xpath('.//div[contains(@class, "p-name p-name-type-2")]/a/em/text()')[0].strip()
        else:
            goods['name'] ='none'
        if product.xpath('.//div[contains(@class, "p-img")]//img[contains(@class, "data-img")]/@src'):
            goods['img'] = product.xpath('.//div[contains(@class, "p-img")]//img[contains(@class, "data-img")]/@src')[
            0].strip()
        else:
            goods['img'] = 'none'
        if product.xpath('.//div[contains(@class, "p-price")]/strong/i/text()'):
            goods['price'] = product.xpath('.//div[contains(@class, "p-price")]/strong/i/text()')[0].strip()
        else:
            goods['price']='none'

        if product.xpath('.//div[contains(@class, "p-commit")]/strong/a/text()'):
            goods['evaluate'] = product.xpath('.//div[contains(@class, "p-commit")]/strong/a/text()')[0].strip()
        else:
            goods['evaluate'] = 'none'
        if product.xpath('.//div[contains(@class, "p-shop")]//a/text()'):
            goods['shop'] = product.xpath('.//div[contains(@class, "p-shop")]//a/text()')[0].strip()
        else:
            goods['shop'] ='none'
        goods_list.append(goods)
    return goods_list



def into_db(goods_list):
    # 创建连接
    coon = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mogujie')

    # 创建游标
    cursor = coon.cursor()
    for goods in goods_list:
        keys=','.join(goods.keys())
        # value=','.join(['%']*len(goods))
        sql = """insert into    weishengsu ({keys}) values ("%s","%s","%s","%s","%s")""".format(keys=keys)

        cursor.execute(sql,tuple(goods.values()))
        coon.commit()
        print('写入成功')
    coon.close()

def main():
    for page in range(2):
        page_source = get_page(page+1)

        goods_list= parse_page(page_source)
        into_db(goods_list)



    # get_tao_page()


if __name__ == '__main__':
    main()
