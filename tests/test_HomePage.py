import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from DataLoad.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getPassword().send_keys("12345678")
        homepage.getCheckbox().click()
        #sel = Select(homepage.getGender())
        #sel.select_by_visible_text("Female")
        self.selectOptionByText(homepage.getGender(),getData["gender"]) #locator,text
        homepage.getSubmit().click()
        alterText = homepage.getSccessMessage().text
        assert ("Success" in alterText)


#more optimized way of dataloading with dictionary by creating another file for data store
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self,request):
       return request.param


#with dictionary dataload
#   @pytest.fixture(params=[{"firstname":"Dipanjana","lastname":"saha","gender":"Female"},{"firstname":"ahon","lastname":"bose","gender":"Male"}])
#   def getData(self,request):
#     return request.param

#with tupple dataload
#    @pytest.fixture(params=[("Dipanjana","Saha","Female"),("Ahon","Bose","Male")])
#    def getData(self,request):
#     return request.param






      #  service_obj = Service(r"C:\Users\Dipanjana Saha\PycharmProjects\chromedriver-win64\chromedriver.exe")
     #   driver = webdriver.Chrome(service=service_obj)
      #  driver.get("https://rahulshettyacademy.com/angularpractice/")
       # driver.maximize_window()
        #driver.find_element(By.CSS_SELECTOR,"[name='name']").send_keys("Dipanjana")


       # driver.find_element(By.NAME,"email").send_keys("Dipa")
       # driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345678")
        #driver.find_element(By.ID, "exampleCheck1").click()
       # sel=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
        #sel.select_by_visible_text("Female")
        #driver.find_element(By.XPATH,"//input[@value='Submit']").click()



       # alterText=driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text

       # assert("Success" in alterText)
