from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.common import CommonOps

class CartDetails(CommonOps):

    CART_ITEM_DETAILS = (By.XPATH,"//span[@class='a-truncate-full a-offscreen']")

    def get_cart_item_details(self):
        cartItemName = self.find(self.CART_ITEM_DETAILS).text
        return cartItemName
   