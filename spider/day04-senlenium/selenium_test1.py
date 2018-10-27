from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree


browser = webdriver.Chrome()

browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 10)

