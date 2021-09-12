from Modules.Pages.BasePage import Page
from Modules.Library.locators import ComputerPageLocators as locators
from selenium.webdriver.support.ui import Select
import logging

class ComputerPage(Page):
    """
    This is the page that appears when a user attempts to add or edit a computer
    """
    logging.basicConfig(level=logging.INFO)
    def __init__(self, driver, url="http://computer-database.herokuapp.com/computers/new"):
        super(ComputerPage, self).__init__(driver, "add_computer_page", url=url)

    def create_computer(self, name=None, introduced_date=None, discontinued_date=None, company=None, cancel=False):
        logging.info(f"Creating computer with params: name={name}, introduced_date={introduced_date}, " 
                     f"discontinued_date={discontinued_date}, company={company}")
        if name:
            name_input = self.driver.find_element_by_id(locators.computer_name)
            name_input.send_keys(name)
        if introduced_date:
            introduced_input = self.driver.find_element_by_id(locators.introduced_date)
            introduced_input.send_keys(introduced_date)
        if discontinued_date:
            discontinued_input = self.driver.find_element_by_id(locators.discontinued_date)
            discontinued_input.send_keys(discontinued_date)
        if company:
            company_dropdown = Select(self.driver.find_element_by_id(locators.company))
            company_dropdown.select_by_visible_text(company)
        if cancel:
            cancel_button = self.driver.find_element_by_xpath(locators.cancel_button)
            cancel_button.click()
        else:
            create_button = self.driver.find_element_by_xpath(locators.create_computer_button)
            create_button.click()

    def edit_computer(self, name=None, introduced_date=None, discontinued_date=None, company=None, cancel=False):
        logging.info(f"Editing computer with params: name={name}, introduced_date={introduced_date}, " 
                     f"discontinued_date={discontinued_date}, company={company}")
        if name:
            name_input = self.driver.find_element_by_id(locators.computer_name)
            name_input.clear()
            name_input.send_keys(name)
        if introduced_date:
            introduced_input = self.driver.find_element_by_id(locators.introduced_date)
            introduced_input.clear()
            introduced_input.send_keys(introduced_date)
        if discontinued_date:
            discontinued_input = self.driver.find_element_by_id(locators.discontinued_date)
            discontinued_input.clear()
            discontinued_input.send_keys(discontinued_date)
        if company:
            company_dropdown = Select(self.driver.find_element_by_id(locators.company))
            company_dropdown.select_by_visible_text(company)
        if cancel:
            cancel_button = self.driver.find_element_by_xpath(locators.cancel_button)
            cancel_button.click()
        else:
            save_computer_button = self.driver.find_element_by_xpath(locators.save_computer_button)
            save_computer_button.click()

    def delete_computer(self):
        """
        Presses the red "Delete this computer" button
        """
        delete_button = self.driver.find_element_by_xpath(locators.delete_computer_button)
        delete_button.click()

