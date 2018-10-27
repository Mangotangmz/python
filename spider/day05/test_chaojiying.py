import time
from io import BytesIO

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urllib.parse import quote
from lxml import etree
from PIL import Image
from chaojiying import main1

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.set_window_size(900, 700)
wait = WebDriverWait(browser, 10)

def get_page():
    """
    获取页面
    :return:
    """
    url = 'http://bm.e21cn.com/log/reg.aspx'
    browser.get(url)
    html = browser.page_source
    return html

def parse_html(html):
    """
    解析页面
    :return:
    """
    # etree_html = etree.HTML(html)
    screenshot = get_full_image()
    screenshot.save('full_image.png')
    x1, y1, x2, y2 = get_position()
    crop_image = screenshot.crop((x1, y1, x2, y2))
    file_name = 'crop.png'
    crop_image.save(file_name)
    captcha = main1(file_name)
    print(captcha)

def get_full_image():
    """
    获取浏览器全图
    :return: 截取的图像对象
    """
    browser.execute_script(('window.scrollTo(0,300)'))
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    return screenshot

def get_position():
    """
    获取验证码的位置（坐标左上角，右下角）
    :return: 验证码的坐标
    """
    img = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#imgCheckCode')))
    time.sleep(2)
    location = img.location
    size = img.size
    x1 = location['x']
    y1 = location['y']
    x2 = location['x'] + size['width']
    y2 = location['y'] + size['height']
    return (x1, y1-300, x2, y2-300)

def main():
    html = get_page()
    parse_html(html)


if __name__ == '__main__':
	main()