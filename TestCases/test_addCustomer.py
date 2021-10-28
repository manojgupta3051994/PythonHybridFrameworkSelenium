from selenium import webdriver
from PageObjects.Login import Login
from TestCases.conftest import setUp
from Utilities.ReadProperties import ReadProp
from Utilities.CustomLogger import Log
from PageObjects.AddCustomerPage import AddCustomer
import string
import random


def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))

class Test_003_AddCustomer:
    URL = ReadProp.readURL()
    username = ReadProp.readUsername()
    password = ReadProp.readPassword()
    logger = Log.Loggie()


    def test_addCustomer(self,setUp):
        self.logger.info("*********Test 003 Add Customer*****************")
        self.driver = setUp
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()
        self.email = random_generator()+'@gmail.com'
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Registered")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Manoj")
        self.addcust.setLastName("Gupta")
        self.addcust.setDob("05/30/1994")
        self.addcust.setCompanyName("DM")
        self.addcust.setAdminContent("Test")
        self.addcust.clickOnSave()
        self.msg = self.driver.find_element_by_tag_name("body").text
        #print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")
        
        