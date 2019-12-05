from poium import Page, PageElement


class BiliPage(Page):
    """哔哩哔哩首页搜索"""
    search_input = PageElement(xpath='//*[@id="nav_searchform"]/input')
    search_button = PageElement(xpath='//*[@id="nav_searchform"]/div/button')
