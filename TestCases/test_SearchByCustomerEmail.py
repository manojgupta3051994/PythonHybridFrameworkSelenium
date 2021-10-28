from selenium import webdriver
from PageObjects.Login import Login
from TestCases.conftest import setUp
from Utilities.ReadProperties import ReadProp
from Utilities.CustomLogger import Log
from PageObjects.SearchCustomerPage import SearchCustomer
from PageObjects.AddCustomerPage import AddCustomer
import time


class test_Search_Customer_by_Email_004 :

    URL = ReadProp.readURL()
    username = ReadProp.readUsername()
    password = ReadProp.readPassword()
    logger = Log.Loggie()

    def test_SearchCustomerByEmail (self,setUp):

        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver=setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")