from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWx():
    def setup(self):
        chromeOptions=Options()
        # 导入options
        # 添加参数
        chromeOptions.add_experimental_option("debuggerAddress","127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chromeOptions)
        # chrome --remote-debugging-port=9222 打开新的窗口
        self.driver.implicitly_wait(3)

    def test_tianjia(self):
        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap div:nth-child(1)").click()
        # 首页直接点击添加成员
        self.driver.find_element(By.ID, "menu_contacts").click()
        sleep(10)
        # 首页点击通讯录，添加显示等待
        element=(By.CSS_SELECTOR, ".js_has_member div:nth-child(1) .js_add_member")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        self.driver.find_element(By.ID, "username").send_keys("abcd")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("1234567")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13512345677")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

    def teardown(self):
        sleep(5)
        self.driver.quit()