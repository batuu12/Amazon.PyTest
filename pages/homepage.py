import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.common import CommonOps


class HomePage(CommonOps):

    SEARCH_BOX = (By.XPATH,"//div[@class='nav-search-field ']//input")
    SEARCH_BUTTON = (By.ID,"nav-search-submit-button")
    CART_BUTTON = (By.ID,"nav-cart-text-container")
    ACCEPT_COOKIES = (By.ID,"sp-cc-accept")

    def accept_cookies(self):
        self.find(self.ACCEPT_COOKIES).click()
        time.sleep(2.0)


    def search_desired_item(self,searchItem):
        self.find(self.SEARCH_BOX).click()
        time.sleep(5)
        self.find(self.SEARCH_BOX).send_keys(searchItem)
        time.sleep(5)
        self.find(self.SEARCH_BUTTON).click()
        time.sleep(5)

    def navigate_to_cart(self):
        self.find(self.CART_BUTTON).click()
        time.sleep(5)


