import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.test_zuoye import TestZy
# 引入脚本
class TestTask(TestZy):
    def setup(self):
        self.driver = webdriver.Firefox()
        # 使用火狐浏览器运行
        self.driver.get("https://testerhome.com")
        self.driver.implicitly_wait(5)



    # def wait(self, timeout, method):
    #     WebDriverWait(self.driver, timeout, method).until(method)
    #
    # def test_case1(self):
    #     self.driver.find_element(By.CSS_SELECTOR, "#main-nav-menu li:nth-child(4)").click()
    #     a=(By.CSS_SELECTOR, '[data-name=霍格沃兹测试学院]')
    #     self.wait(10, expected_conditions.element_to_be_clickable(a))
    #     self.driver.find_element(*a).click()
    #     self.driver.find_element(By.CSS_SELECTOR, ".topic:nth-child(1) .title a").click()
    #     # 此处:nth-child(1)可去掉，element默认选择第一个；使用elements时必须添加
    #
    # def test_lianjie(self):
    #     self.driver.get("https://testerhome.com/topics/21805")
    #     self.driver.find_element(By.PARTIAL_LINK_TEXT, "第六届中国互联网测试开发大会").click()
    #     print(self.driver.window_handles)
    #     # 打印链接
    #     self.wait(10, lambda x: len(self.driver.window_handles) > 1)
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     # 切换到第二个窗口
    #     self.driver.find_element(By.LINK_TEXT, '演讲申请').click()
    #
    # def teardown_method(self):
    #     time.sleep(5)
    #     self.driver.quit()