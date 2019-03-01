from pageobjects_luntan_2.base_luntan import basepage
from selenium.webdriver.common.by import By
class Public(basepage):
    home_page_moren_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")  # Ĭ�ϰ��
    home_page_fatie_loc = (By.ID, "newspecial")  # ��ʼ������ť
    home_page_title_loc = (By.NAME, "subject")  # ��Ŀ
    home_page_content_loc = (By.TAG_NAME, "body")  # ����
    home_page_post_click_loc = (By.CSS_SELECTOR, ".pnpost span")  # �������Ӱ�ť

    def public(self, title, content):
        self.click(*self.home_page_moren_loc)  # ���Ĭ�ϰ��
        self.click(*self.home_page_fatie_loc)  # �����ʼ������ť
        handle = self.driver.current_window_handle
        self.sendkeys(title, *self.home_page_title_loc)  # ���뷢����Ŀ
        self.driver.switch_to.frame(0)  # ��λ���ݵ�ifram
        self.sendkeys(content, *self.home_page_content_loc)  # ������������
        self.driver.switch_to.window(handle)  # �ص���ǰҳ��Ĵ���
        self.click(*self.home_page_post_click_loc)  # ����������ӵİ�ť