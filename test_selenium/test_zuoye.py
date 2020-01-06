import os
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestZy:

    def setup(self):
        browser=os.getenv("browser", "").lower()
        # 默认使用Chrome
        if browser=="headless":
            self.driver = webdriver.PhantomJS()
        elif browser=="firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver=webdriver.Chrome()
        # 无法使用命令运行
        # self.driver = webdriver.Chrome()
        # self.driver=webdriver.Firefox()
        self.driver.get("https://testerhome.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_lx2(self):
        self.driver.find_element(By.CSS_SELECTOR,'[title="MTSC2020 中国互联网测试开发大会议题征集"]').click()
        self.driver.find_element(By.CSS_SELECTOR,'[data-toggle="dropdown"]').click()
        element1=By.CSS_SELECTOR, '.list-container li:nth-child(4) a '
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element1))
        self.driver.find_element(*element1).click()

    def test_shetuan(self):
        self.driver.find_element(By.CSS_SELECTOR, "#main-nav-menu li:nth-child(4)").click()
        element=By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]'
        WebDriverWait(self.driver, 4).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    def test_jinshuju(self):
        self.driver.get("https://testerhome.com/topics/21495")
        element3=(By.CSS_SELECTOR, ".published-form__submit")
        self.driver.switch_to.frame(0)
        # switch_to.frame切换窗口
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element3))
        self.driver.find_element(By.CSS_SELECTOR, ".published-form__submit").click()

    def test_lianjie(self):
        self.driver.get("https://testerhome.com/topics/21805")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "第六届中国互联网测试开发大会").click()
        print(self.driver.window_handles)
        # 打印链接
        self.driver.switch_to.window(self.driver.window_handles[1])
        # 切换到第二个窗口
        self.driver.find_element(By.LINK_TEXT, '演讲申请').click()

    def teardown_method(self):
        sleep(5)
        self.driver.quit()
