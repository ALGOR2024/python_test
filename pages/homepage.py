from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://demoblaze.com/index.html')

    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_products_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count

    def laptops(self):
        laptops_link= self.browser.find_element(By.CSS_SELECTOR, '''[onclick = "byCat('notebook')"]''')
        laptops_link.click()

    def check_dell_price(self,price):
        dell_price = self.browser.find_element(By.CSS_SELECTOR, '.price-container')
        assert price in dell_price.text


