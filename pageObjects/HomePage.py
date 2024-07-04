from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver=driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    #driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys("Dipanjana")
    home=(By.CSS_SELECTOR, "[name='name']")
    #driver.find_element(By.NAME, "email").send_keys("Dipa")
    email=(By.NAME, "email")
    #driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345678")
    password=(By.ID,"exampleInputPassword1")
    #driver.find_element(By.ID, "exampleCheck1").click()
    checkbox=(By.ID, "exampleCheck1")
    #driver.find_element(By.ID, "exampleFormControlSelect1")
    gender=(By.ID, "exampleFormControlSelect1")

    # driver.find_element(By.XPATH,"//input[@value='Submit']").click()
    submit=(By.XPATH,"//input[@value='Submit']")
    # alterText = driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
    SccessMessage=(By.CSS_SELECTOR, "[class*='alert-success']")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.home)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)
    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)
    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    def getSccessMessage(self):
        return self.driver.find_element(*HomePage.SccessMessage)

