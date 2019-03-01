
from pageobjects_luntan_3.base_luntan import basepage
from selenium.webdriver.common.by import By
class Login(basepage):
    home_page_input_yonghu_search_loc=(By.ID,"ls_username")#��λ�û���
    home_page_input_pwd_search_loc = (By.ID, "ls_password")#�����
    home_page_button_loc=(By.CSS_SELECTOR, "em")#��¼��ť

    def login(self,admin,pwd):
        self.sendkeys(admin,*self.home_page_input_yonghu_search_loc)#�����û�
        self.sendkeys(pwd, *self.home_page_input_pwd_search_loc)#��������
        self.click(*self.home_page_button_loc)#�����¼





