from pageobjects_luntan_2.base_luntan import basepage
from selenium.webdriver.common.by import By
class Delete(basepage):
    home_page_moren_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")  # Ĭ�ϰ��
    home_page_selete_loc = (By.NAME, "moderate[]")  # ��ʼ������ť
    home_page_delete_loc=(By.CSS_SELECTOR,"#mdly strong:nth-child(1) a")#ѡ��ɾ��
    home_page_confirm_loc=(By.ID,"modsubmit")#��λȷ����λ��

    # home_page_title_loc = (By.NAME, "subject")  # ��Ŀ
    # home_page_content_loc = (By.TAG_NAME, "body")  # ����
    # home_page_post_click_loc = (By.CSS_SELECTOR, ".pnpost span")  # �������Ӱ�ť

    def Delete(self):
        self.click(*self.home_page_moren_loc)  # ���Ĭ�ϰ��
        self.click(*self.home_page_selete_loc)  # ѡ��ɾ���Ŀ�
        self.click(*self.home_page_delete_loc)#���ɾ��
        self.click(*self.home_page_confirm_loc)#���ȷ����ť

        # handle = self.driver.current_window_handle
        # self.sendkeys(title, *self.home_page_title_loc)  # ���뷢����Ŀ
        # self.driver.switch_to.frame(0)  # ��λ���ݵ�ifram
        # self.sendkeys(content, *self.home_page_content_loc)  # ������������
        # self.driver.switch_to.window(handle)  # �ص���ǰҳ��Ĵ���
        # self.click(*self.home_page_post_click_loc)  # ����������ӵİ�ť