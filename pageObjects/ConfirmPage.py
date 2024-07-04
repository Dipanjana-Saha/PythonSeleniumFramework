from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver=driver
    #self.driver.find_element(By.ID, "country").send_keys("ind")
    country=(By.ID, "country")

    #self.driver.find_element(By.LINK_TEXT,"India").click()
    click_country=(By.LINK_TEXT,"India")

    #self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
    checkBox=(By.XPATH,"//div[@class='checkbox checkbox-primary']")

    #self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
    PurchaseButton= (By.CSS_SELECTOR,"[type='submit']")
    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)
    def getClickCountry(self):
        return self.driver.find_element(*ConfirmPage.click_country)
    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)
    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.PurchaseButton)

