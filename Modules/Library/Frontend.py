import logging
from Modules.Pages.HomePage import HomePage
from Modules.Pages.ComputerPage import ComputerPage
from selenium import webdriver

class WebUI:
    #could add more drivers like Firefox/Safari in the future
    driver = None

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        logging.info("Creating Chrome Browser Driver")
        self.driver = webdriver.Chrome()
        logging.info("Creating Pages")
        self.home_page = HomePage(self.driver)
        self.computer_page = ComputerPage(self.driver)


