import time

from selenium.webdriver.common.by import By

class Homepage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://student.fbtuit.uz/dashboard/login')

    def input_login(self,login,password):
        enterlogin = self.browser.find_element(By.ID, 'formstudentlogin-login')
        enterlogin.send_keys(login)
        enterpassword = self.browser.find_element(By.ID, 'formstudentlogin-password')
        enterpassword.send_keys(password)
        button = self.browser.find_element(By.XPATH, "//button[text()='Kirish']")
        button.click()
        time.sleep(5)
        time_table= self.browser.find_element(By.CSS_SELECTOR, '[href="/education/time-table"]')
        time_table.click()
        time.sleep(30)