from pageobjects_luntan_4.base_luntan import basepage
from selenium.webdriver.common.by import By
class Vote(basepage):
    first_selete_loc=(By.ID,"option_1")#��λ��һ��ѡ���
    sumbit_button_loc=(By.NAME,"pollsubmit")#��λ���ύ��ť

    def vote(self):
        self.click(*self.first_selete_loc)#�����һ��ѡ���
        self.click(*self.sumbit_button_loc)#����ύ��ť

