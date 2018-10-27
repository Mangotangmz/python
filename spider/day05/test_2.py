
import time
from io import BytesIO
from selenium.webdriver.support import expected_conditions as EC

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
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.set_window_size(900, 700)
wait = WebDriverWait(browser, 10)

def get_page():
    """
    获取页面
    :return:
    """
    url = 'http://www.cdpta.gov.cn/frt/register/preLogin.do'
    browser.get(url)
    html = browser.page_source
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#btnSubmit')))
    submit.click()
    return html

def parse_html(html):
    """
    解析页面
    :return:
    """
    etree_html = etree.HTML(html)

    screenshot = get_full_image()
    screenshot.save('full_image.png')
    x1, y1, x2, y2 = get_position()
    crop_image = screenshot.crop((x1, y1, x2, y2))
    file_name = 'crop.png'
    crop_image.save(file_name)
    captcha = main1(file_name)
    print(captcha)

    # input_username = wait.until(expected_conditions.presence_of_element_located
    #                             ((By.CSS_SELECTOR, 'input#username')))
    # input_password1 = wait.until(expected_conditions.presence_of_element_located
    #                              ((By.CSS_SELECTOR, 'input#pwd')))
    # input_password2 = wait.until(expected_conditions.presence_of_element_located
    #                              ((By.CSS_SELECTOR, 'input#pwd_Q')))
    # input_tel = wait.until(expected_conditions.presence_of_element_located
    #                        ((By.CSS_SELECTOR, 'input#tel')))
    # input_check = wait.until(expected_conditions.presence_of_element_located
    #                          ((By.CSS_SELECTOR, 'input#CheckCode')))
    # sublime = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input#btn_login')))
    # username = 'lalala'
    # password = '123456'
    # tel = '18011405897'
    #
    # input_username.send_keys(username)
    # input_password1.send_keys(password)
    # input_password2.send_keys(password)
    # input_tel.send_keys(tel)
    # input_check.send_keys(captcha)
    # time.sleep(2)
    # sublime.click()

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
    img = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#yzmimg')))
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