from selenium import webdriver
from PageObjects.Login import Login
from TestCases.conftest import setUp
from Utilities.ReadProperties import ReadProp
from Utilities.CustomLogger import Log



class Test_001_Login:

    URL = ReadProp.readURL()
    username = ReadProp.readUsername()
    password = ReadProp.readPassword()
    logger = Log.Loggie()

    def test_HomePageTitle(self,setUp):
        self.logger.info("************ Test_001_Login ***********************")
        self.logger.info("************ Verifying Test ***********************")
        #self.driver = webdriver.Chrome(executable_path=r'C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe')
        self.driver = setUp
        self.driver.get(self.URL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            self.logger.info("************ Test Passed ***********************")
            assert  True
        else:
            self.driver.save_screenshot(r".\\env\Screenshots\\"+"test_HomePageTitle.png")
            self.logger.info("************ Test Failed ***********************")
            assert False

        

    def test_login(self,setUp):
        #self.driver = webdriver.Chrome(executable_path=r'C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe')
        self.driver = setUp
        self.driver.get(self.URL)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickRemember()
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == 'Dashboard / nopCommerce administration':
            assert True
        else:
            self.driver.save_screenshot(r".\\env\Screenshots\\"+"test_login.png")
            assert False
        