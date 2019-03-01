# -*- coding: GBK -*-
from pageobjects_luntan_2.base_luntan import basepage
from selenium.webdriver.common.by import By
import time
class Add(basepage):
    admin_center_loc = (By.LINK_TEXT,"��������")  # ��λ��������
    forum_loc=(By.CSS_SELECTOR,"#topmenu li:nth-child(7) a")#��λ��̳
    add_new_module_loc=(By.LINK_TEXT,"����°��")#��λ����°��
    submit_button_loc=(By.ID,"submit_editsubmit")#��λȷ����ť


    def add(self):
        self.click(*self.admin_center_loc)  # �����������
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(10)
        self.click(*self.forum_loc)#�����̳
        self.driver.switch_to.frame(0)
        self.click(*self.add_new_module_loc)#�������µİ��
        self.click(*self.submit_button_loc)#����ύ��ť
        self.driver.close()
        self.driver.switch_to.window(handles[0])

