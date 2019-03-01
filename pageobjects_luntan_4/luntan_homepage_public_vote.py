# -*- coding: GBK -*-
from pageobjects_luntan_4.base_luntan import basepage
from selenium.webdriver.common.by import By
class Public(basepage):
    home_page_moren_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")  # Ĭ�ϰ��
    home_page_fatie_loc = (By.ID, "newspecial")  # ��ʼ������ť
    vote_loc=(By.LINK_TEXT,"����ͶƱ")#��λ����ͶƱ��λ��
    text_input_loc=(By.NAME,"subject")#��λ��ͶƱ��Ŀ��λ��
    first_tag_vote_loc=(By.CSS_SELECTOR,"#pollm_c_1 p:nth-child(1) input")#��λ����һ��ѡ���λ��
    second_tag_vote_loc = (By.CSS_SELECTOR, "#pollm_c_1 p:nth-child(2) input")  # ��λ���ڶ���ѡ���λ��
    third_tag_vote_loc = (By.CSS_SELECTOR, "#pollm_c_1 p:nth-child(3) input")  # ��λ��������ѡ���λ��
    public_vote_button_loc=(By.CSS_SELECTOR,".pnpost span")#��λ������ͶƱ��λ��

    # home_page_title_loc = (By.NAME, "subject")  # ��Ŀ
    # home_page_content_loc = (By.TAG_NAME, "body")  # ����
    # home_page_post_click_loc = (By.CSS_SELECTOR, ".pnpost span")  # �������Ӱ�ť

    def public(self, title, first,second,third):
        self.click(*self.home_page_moren_loc)  # ���Ĭ�ϰ��
        self.click(*self.home_page_fatie_loc)  # �����ʼ������ť
        self.click(*self.vote_loc)#�������ͶƱ
        handle = self.driver.current_window_handle
        self.sendkeys(title,*self.text_input_loc)#����ͶƱ����Ŀ
        self.sendkeys(first,*self.first_tag_vote_loc)#�����һ��ѡ�����Ŀ
        self.sendkeys(second, *self.second_tag_vote_loc)  # ����ڶ���ѡ�����Ŀ
        self.sendkeys(third, *self.third_tag_vote_loc)  # ���������ѡ�����Ŀ
        self.driver.switch_to.window(handle)  # �ص���ǰҳ��Ĵ���
        self.click(*self.public_vote_button_loc)#���ͶƱ��ť

        # self.sendkeys(title, *self.home_page_title_loc)  # ���뷢����Ŀ
        # self.driver.switch_to.frame(0)  # ��λ���ݵ�ifram
        # self.sendkeys(content, *self.home_page_content_loc)  # ������������
        # self.driver.switch_to.window(handle)  # �ص���ǰҳ��Ĵ���
        # self.click(*self.home_page_post_click_loc)  # ����������ӵİ�ť