import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lxml import etree
import time
from PIL import Image
from chaojiying import main1
from io import BytesIO


browser = webdriver.Chrome()
browser.set_window_size(1300, 600)
wait = WebDriverWait(browser, 10)


def get_page():
    url = 'http://bm.e21cn.com/log/reg.aspx'
    browser.get(url)
    html = browser.page_source
    return html


def get_msg(html):
    etree_html = etree.HTML(html)
    username = 'lalala'
    password = '123456'
    tel = '18011405897'
    img_url = etree_html.xpath('//img[@id="imgCheckCode"]/@src')
    check_url = 'http://bm.e21cn.com' + img_url[0][2:]
    img = get_geetest_image('1.png')
    print(img)
    # headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"}
    # response = requests.get(url=check_url, headers=headers)
    # time.sleep(5)
    # with open('./yanzhengma/1.jpg', 'wb') as f:
    #     f.write(response.content)
    check_msg = main1('1.png')
    print(check_msg)
    input_username = wait.until(expected_conditions.presence_of_element_located
                       ((By.CSS_SELECTOR, 'input#username')))
    input_password1 = wait.until(expected_conditions.presence_of_element_located
                       ((By.CSS_SELECTOR, 'input#pwd')))
    input_password2 = wait.until(expected_conditions.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#pwd_Q')))
    input_tel = wait.until(expected_conditions.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#tel')))
    input_check = wait.until(expected_conditions.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#CheckCode')))
    sublime = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#btn_login')))
    input_username.send_keys(username)
    input_password1.send_keys(password)
    input_password2.send_keys(password)
    input_tel.send_keys(tel)
    input_check.send_keys(check_msg)
    time.sleep(2)
    sublime.click()


def get_position():
    """
    获取验证码位置
    :return: 验证码位置元组
    """
    img = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#imgCheckCode')))
    time.sleep(2)
    location = img.location
    size = img.size
    print(size)
    top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
        'width']
    return (top, bottom, left, right)


def get_screenshot():
    """
    获取网页截图
    :return: 截图对象
    """
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    return screenshot


def get_geetest_image(name):
    """
    获取验证码图片
    :return: 图片对象
    """
    top, bottom, left, right = get_position()
    print('验证码位置', top, bottom, left, right)
    screenshot = get_screenshot()
    captcha = screenshot.crop((left, top, right, bottom))
    path = name
    captcha.save(path)
    return captcha


def main():
    html = get_page()
    get_msg(html)


if __name__ == '__main__':
    main()