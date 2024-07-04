from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self,driver):
        self.driver=driver
    #cards = self.driver.find_elements(By.CSS_SELECTOR,".card-title a")
    cardTitle= (By.CSS_SELECTOR,".card-title a")
    #self.driver.find_element(By.CSS_SELECTOR,".card-footer button")
    cardFooter=(By.CSS_SELECTOR,".card-footer button")
    #self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']")
    cardCheckOut= (By.CSS_SELECTOR,"a[class*='btn-primary']")

    # self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
    checkout= (By.XPATH,"//button[@class='btn btn-success']")
    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)

    def getCheckOut(self):
        return self.driver.find_element(*CheckoutPage.cardCheckOut)

    def CheckOutItems(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

