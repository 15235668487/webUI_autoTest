# -*- coding: GBK -*-
from pageobjects_luntan_2.base_luntan import basepage
from selenium.webdriver.common.by import By
class Exit(basepage):
    home_page_post_reply_quit_loc = (By.LINK_TEXT, "�˳�")  # ��λ�˳�

    def exit(self):
        self.click(*self.home_page_post_reply_quit_loc)  # ����˳���ť
