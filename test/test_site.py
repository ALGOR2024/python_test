from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.hemishome import Homepage
from pages.homepage import HomePage
from pages.product import ProductPage
import pytest
import conftest
from conftest import browser

def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')
    #galaxy_s6 = browser.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    #galaxy_s6.send_keys('login')

def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_products_count(2)



def test_dell_price(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.laptops()
    time.sleep(2)
    dell_i7_8gb = browser.find_element(By.LINK_TEXT, 'Dell i7 8gb')
    dell_i7_8gb.click()
    homepage.check_dell_price("$700")


def test_hemis_login(browser):
    hemishome = Homepage(browser)
    hemishome.open()
    hemishome.input_login('392211100150','Asilbek2003')


