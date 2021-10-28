from selenium import webdriver
from PageObjects.Login import Login
from TestCases.conftest import setUp
from Utilities.ReadProperties import ReadProp
from Utilities.CustomLogger import Log
from Utilities import XLUtils
import time

class Test_DDT_Login_001:
    
    baseURL = ReadProp.readURL()
    path = r"C:\Users\Manoj\Desktop\Python - Selenium Practice\HDD\env\TestData\LoginData.xlsx"
    logger = Log.Loggie()
    Status = []

    def test_login_ddt(self,setUp):
        self.logger.info("************ Test_001_DDT_Login ***********************")
        self.logger.info("************ Verifying Test ***********************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        for i in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',i,1)
            self.password = XLUtils.readData(self.path,'Sheet1',i,2)
            self.expected = XLUtils.readData(self.path,'Sheet1',i,3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            exp_title = "Dashboard / nopCommerce administration"
            act_title = self.driver.title
            if act_title == exp_title:
                if self.expected == 'Pass':
                    self.logger.info("*****Passed*****")
                    self.lp.clickLogout()
                    self.Status.append("Pass")
                elif self.expected == 'Fail':
                    self.logger.info("*****Failed*****")
                    self.lp.clickLogout()
                    self.Status.append("Failed")
            elif act_title != exp_title:
                if self.expected == 'Pass':
                    self.logger.info("*****Failed*****")
                    self.Status.append("Failed")
                elif self.expected == 'Fail':
                    self.logger.info("*****Passed*****")
                    self.Status.append("Passed")
        if "Fail" not in self.Status:
            self.logger.info("*****Login DDT Test Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****Login DDT Test Failed")
            self.driver.close()
            assert False

        self.logger.info("********** End of DDT Login Test **************")
            







