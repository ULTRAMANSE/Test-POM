import os
from selenium import webdriver

BaseDir = os.path.dirname(os.path.abspath(__file__))
ReportDir = BaseDir + "/reportdir/"
CaseDir = './testcase/'
# 所要运行的url
url = "https://www.bilibili.com/"
# 浏览器类型
DriverType = 'chrome'


def brower():
    """
    定义浏览器驱动
    :return:
    """
    global driver
    global DriverType
    
    if DriverType == "chrome":
        # 谷歌浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()
    
    if DriverType == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    
    return driver


def close_brower():
    yield webdriver
    driver.quit()
    print("test is end")
