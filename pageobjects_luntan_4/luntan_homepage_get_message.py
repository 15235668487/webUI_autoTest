# -*- coding: GBK -*-
from pageobjects_luntan_4.base_luntan import basepage
from selenium.webdriver.common.by import By
class Get_Message(basepage):
    title_loc=(By.ID,"thread_subject")#��λͶƱ��Ŀ
    first_title_loc=(By.CSS_SELECTOR,".pcht tr:first-of-type label")#��λ��һ��ѡ������
    second_title_loc = (By.CSS_SELECTOR, ".pcht tr:nth-child(3) label")  # ��λ��һ��ѡ������
    third_title_loc = (By.CSS_SELECTOR, ".pcht tr:nth-child(5) label")  # ��λ��һ��ѡ������
    first_percent_loc = (By.CSS_SELECTOR, ".pcht tr:nth-child(2) td:nth-child(2)")  # ��λ��һ������
    second_percent_loc = (By.CSS_SELECTOR, ".pcht tr:nth-child(4) td:nth-child(2)")  # ��λ�ڶ�������
    third_percent_loc = (By.CSS_SELECTOR, ".pcht tr:nth-child(6) td:nth-child(2)")  # ��λ����������


    # sumbit_button_loc=(By.NAME,"pollsubmit")#��λ���ύ��ť

    def get_message(self):
        print("����ͶƱ�ı���Ϊ��")
        self.get_text(*self.title_loc)  # ��ȡͶƱ����
        print(self.get_text(*self.first_title_loc))#��ȡ��һ��ͶƱѡ�����Ŀ
        print("ͶƱ����Ϊ��")
        self.get_text(*self.first_percent_loc)# ��ȡ��һ��ͶƱ�ı���
        print(self.get_text(*self.second_title_loc))#��ȡ�ڶ���ͶƱѡ�����Ŀ
        print("ͶƱ����Ϊ��")
        self.get_text(*self.second_percent_loc) # ��ȡ�ڶ���ͶƱ�ı���
        print(self.get_text(*self.third_title_loc))  # ��ȡ������ͶƱѡ�����Ŀ
        print("ͶƱ����Ϊ��")
        self.get_text(*self.third_percent_loc) # ��ȡ������ͶƱ�ı���



