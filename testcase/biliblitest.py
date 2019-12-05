import unittest
from config import brower, url
from page.bili_page import BiliPage
from selenium import webdriver


class Bili(unittest.TestCase):
    """搜索功能测试"""
    
    def test_bili_case(self):
        page = BiliPage(brower())
        page.get(url)
        page.search_input = "假面骑士"
        page.search_button.click()
