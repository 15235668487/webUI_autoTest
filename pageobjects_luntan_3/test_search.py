# -*- coding: GBK -*-
from pageobjects_luntan_3.base_luntan import basepage
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
class Search(basepage):
    search_loc=(By.NAME,"searchsubmit")#��λ������ť
    gaoji_loc=(By.LINK_TEXT,"�߼�")#��λ�߼�
    test_loc=(By.ID,"srchtxt_1")#��λ�����
    selete_loc=(By.NAME,"srchtype")#��λ��ѡ��
    find_loc=(By.CSS_SELECTOR,".pnc")#��λ���Ұ�ť
    condition_loc=(By.CSS_SELECTOR,".xs3 strong font")#��λcondition
    # title_loc=(By.ID,"thread_subject")#��ȡ��ǰ��������Ŀ

    def search(self,content):
        self.click(*self.search_loc)#���������ť
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.click(*self.gaoji_loc)#����߼�
        self.sendkeys(content,*self.test_loc)#������������
        self.click(*self.selete_loc)#�����ѡ��
        self.click(*self.find_loc)#�������
        self.click(*self.condition_loc)#�����������������
        aaaaa = self.driver.window_handles
        self.driver.switch_to.window(aaaaa[2])
        # self.get_text(*self.title_loc)#���text
        assert "haotest" in self.driver.title
