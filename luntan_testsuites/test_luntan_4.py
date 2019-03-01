#-*- coding: GBK -*-
import unittest
from selenium.webdriver.common.by import By
from luntan_testsuites.base_luntan_testcase import BaseTestCase
from pageobjects_luntan_4.luntan_homepage_login import Login
from pageobjects_luntan_4.luntan_exit import Exit
from pageobjects_luntan_4.luntan_homepage_public_vote import Public
from pageobjects_luntan_4.luntan_homepage_vote import Vote
from pageobjects_luntan_4.luntan_homepage_get_message import Get_Message
import time
class Test_4(BaseTestCase):
    def test_luntan_4(self):
        log = Login(self.driver)
        log.login("sunkai", "19960618")
        self.assertEqual(log.find_element(By.LINK_TEXT, "��������").text, "��������")
        time.sleep(2)
        p=Public(self.driver)
        p.public("�ֻ�ͶƱ","��Ϊ","��С��","��ƻ��")
        self.assertNotEqual(p.find_element(By.ID, "thread_subject").text, '')


        #ͶƱ
        vo=Vote(self.driver)
        vo.vote()
        self.assertEqual(vo.find_element(By.CSS_SELECTOR,".pcht tr:nth-child(7) td").text,"���Ѿ�Ͷ��Ʊ��лл���Ĳ���")

        #��ȡ��Ϣ
        ge=Get_Message(self.driver)
        ge.get_message()


        # se=Search(self.driver)
        # se.search("haotest")
        # ex=Exit(self.driver)
        # ex.exit()
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()