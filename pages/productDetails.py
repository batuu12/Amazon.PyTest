import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.common import CommonOps

class ProductDetails(CommonOps):

    PRODUCT_NAME = (By.ID,"productTitle")
    ADD_TO_CART_BUTTON = (By.NAME,"submit.add-to-cart")
    ADD_CART_DETAILS = (By.CLASS_NAME,"//span[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']")

    def add_to_cart_desired_item(self):
        self.find(self.ADD_TO_CART_BUTTON).click()
        time.sleep(5)
      
    def get_product_text(self):
        productName = self.find(self.PRODUCT_NAME).text
        return productName

