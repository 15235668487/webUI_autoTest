from pageobjects_luntan_2.base_luntan import basepage
from selenium.webdriver.common.by import By
class Reply(basepage):
    home_page_post_reply_loc = (By.ID, "post_reply")  # ��λ����
    home_page_post_reply_content = (By.ID, "postmessage")  # ��λ������
    home_page_post_reply_button_loc = (By.ID, "postsubmit")  # ��λ������ť
    def reply(self,post_content):
        self.click(*self.home_page_post_reply_loc)  # ���������ť
        self.sendkeys(post_content, *self.home_page_post_reply_content)  # ���ͻ�������
        self.click(*self.home_page_post_reply_button_loc)  # �������/���밴ť