"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as ff_opt
from selenium.webdriver.chrome.options import Options as chr_opt
import os

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://letskodeit.teachable.com/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
            driver.implicitly_wait(5)
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
            driver.set_window_size(1680, 1000)
            driver.implicitly_wait(5)
        elif self.browser == "firefox_hdls":
            # driver = webdriver.Firefox()
            options = ff_opt()
            options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
            driver.set_window_size(1680, 1000)
            driver.implicitly_wait(5)
        elif self.browser == "chrome":
            chromedriver = "/Users/marten.westman/Applications/Selenium/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
            driver.set_window_size(1680, 1000)
            driver.implicitly_wait(5)
        elif self.browser == "chrome_hdls":
            # Set chrome driver
            chromedriver = "/Users/marten.westman/Applications/Selenium/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            # driver = webdriver.Chrome(chromedriver)
            options = chr_opt()
            options.headless = True
            driver = webdriver.Chrome(chromedriver, options=options)
            driver.set_window_size(1680, 1000)
            driver.implicitly_wait(5)
            # driver.maximize_window()

        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(5)
        # Maximize the window
        # driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver