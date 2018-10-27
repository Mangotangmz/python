import requests
import re
from lxml import etree


def get_one_page():
    url = ""
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None


def parse_with_xpath(html):
    etree_html = etree.HTML(html)
    # print(etree_html)
    # 查找元素所有子孙节点 //
    # result = etree_html.xpath('//div[@class="rank"]/ul/li/a/@title')
    # print(result)
    # #
    # result = etree_html.xpath('//li/attribute::*')
    # print(result)

    #图片
    result = etree_html.xpath('')
    print(result)

    # result = etree_html.xpath('//img/@src')
    # print(result)

    # result = etree_html.xpath('//div/p/text()')
    # print(result)

    # result = etree_html.xpath('//*/text()')
    # print(result)
    # print(len(result))

def main():
    html = get_one_page()
    print(html)
    parse_with_xpath(html)


if __name__ == '__main__':
    main()
