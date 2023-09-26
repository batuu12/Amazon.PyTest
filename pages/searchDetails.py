import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.common import CommonOps

class SearchDetails(CommonOps):

    FIRST_ITEM = (By.XPATH,"//div[@data-cel-widget='search_result_2']")
    #ITEM_EX = (By.XPATH,"//span[text()='Apple iPhone 12 (128 GB) - Siyah']")
    MIN_VALUE_INPUT = (By.XPATH,"//input[@id='low-price']")
    MAX_VALUE_INPUT = (By.XPATH,"//input[@id='high-price']")
    FILTER_VALUE_BUTTON = (By.XPATH,"//input[@id='high-price']/following-sibling::span//input")
    NO_RESULT_TEXT = (By.XPATH,"//span[contains(text(),'sonuç yok.')]")
    MAINPAGE = (By.TAG_NAME,"html")

    def click_desired_item(self):
        try:
            self.find(self.MAINPAGE).send_keys(Keys.ARROW_DOWN)
            self.find(self.FIRST_ITEM).click()
            time.sleep(5)
            return ("Item has seen")
        except NoSuchElementException:
            return ("Item not seen")
        except ElementNotInteractableException:
            return ("Element not Interactable")

    def set_min_value(self,minValue):
        self.find(self.MAINPAGE).send_keys(Keys.ARROW_DOWN)
        time.sleep(5)
        self.find(self.MAINPAGE).send_keys(Keys.ARROW_DOWN)
        time.sleep(5)
        self.find(self.MIN_VALUE_INPUT).click()
        time.sleep(5)
        self.find(self.MIN_VALUE_INPUT).send_keys(minValue)
        time.sleep(5)

    def set_max_value(self,maxValue):
        self.find(self.MIN_VALUE_INPUT).click()
        time.sleep(5)
        self.find(self.MAX_VALUE_INPUT).send_keys(maxValue)
        time.sleep(5)

    def filter_desired_values(self):
        self.find(self.FILTER_VALUE_BUTTON).click()
        time.sleep(5)

    def is_Result_Ok_Or_Not(self):
        result = self.find(self.NO_RESULT_TEXT).is_displayed()
        time.sleep(5)
        return result
    