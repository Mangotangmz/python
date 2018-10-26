import re

import requests
import json


def get_one_page(offset):
    url = "https://maoyan.com/board/4?offset=%d" % offset
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None


def get_all_page():
    for i in range(11):
        print(i)
        offset = i * 10
        html = get_one_page(offset)
        list = parse_one_page(html)
        # print(items)
        for j in list.image:
            write_img(j)
            print(j)


def parse_one_page(html):
    list = []

    # 获取主演
    item_actor = re.compile('<p class="star">(.*?)</p>', re.S)

    # 获取上映时间
    item_time = re.compile('<p class="releasetime">(.*?)</p>', re.S)
    item_image = re.compile('movieId.*?>.*?<img.*?<img.*?src="(.*?)"', re.S)
    # 获取图片链接
    # pattern = re.compile(r'<i class="board-index board-index-\d*?">(.*?)</i>', re.S)
    # pattern = re.compile('', re.S)
    items_actor = re.findall(item_actor, html)
    items_time = re.findall(item_time, html)
    items_image = re.findall(item_image, html)

    for i in range(9):
        one_movie = {}
        one_movie['actor'] = items_actor[i]
        one_movie['time'] = items_time[i]
        one_movie['image'] = items_image[i]
        list.append(one_movie)
    return list


def main():
    into_json()
    # get_all_page()
    # items = parse_one_page(html)
    # for item in items:
    #     write_img(item)
    #     print(item.strip())

    # print(html)


def write_img(url):
    url_parts = url.split("@")
    url_result = url_parts[0]
    filename = "./images/%s" % url_result.split("/")[-1]
    # print(filename)

    # 得到响应对象
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)


# 将图片以jason格式存储图片
def into_json():
    # for i in range(11):
    #     print(i)
    #     offset = i * 10
    html = get_one_page(0)
    list = parse_one_page(html)

    new_dict = json.dumps(str(list),ensure_ascii=False)
    with open("./json/record.json", "w") as f:
        f.write(new_dict)
        print("写入文件完成...")
    return None


if __name__ == '__main__':
    main()
