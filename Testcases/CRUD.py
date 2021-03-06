from datetime import datetime, timedelta
from Modules.Library.Frontend import WebUI
from Modules.Library.Backend import Backend
from Modules.Library.locators import HomePageLocators, ComputerPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
import pytest
import random
import string


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class TestCRUD:
    """
    Automated testcases relating to the Anni-NetflixTestPlan test plan. Testcases that are covered will have "Automated" in their columns.
    """
    logging.basicConfig(level=logging.INFO)
    creation_failure = False

    @classmethod
    def setup_class(cls):
        cls.ui = WebUI()
        cls.backend = Backend()
        #generating name to use for creating computer
        name = id_generator()
        cls.computer_name = name

    @classmethod
    def teardown_class(cls):
        cls.ui.driver.close()
        cls.ui.driver.quit()

### ----CREATE---- ###
    def test_create_computer_happy_path(self):
        """
        Creates a new computer with all the parameters filled out.
        This corresponds to testcase C1 in the manual test plan
        """
        self.ui.home_page.open_page()
        original_computer_count = self.ui.home_page.get_computer_count()
        logging.info(f"Original computer count: {original_computer_count}")
        self.ui.home_page.click_add_computer()
        today = datetime.today().strftime('%Y-%m-%d')
        yesterday = datetime.today() - timedelta(days=1)
        formatted_yesterday = datetime.strftime(yesterday, '%Y-%m-%d')
        company = "RCA"
        self.ui.computer_page.create_computer(name=self.computer_name, introduced_date=formatted_yesterday,
                                                  discontinued_date=today, company=company)
        WebDriverWait(self.ui.driver, 5).until(
            EC.visibility_of_element_located((By.ID, HomePageLocators.add_button))
        )
        try:
            assert "has been created" in self.ui.driver.find_element_by_xpath(HomePageLocators.banner).text
        except:
            logging.info("Skipping next related testcases if creating computer fails")
            self.__class_.creation_failure = True
        new_count = self.ui.home_page.get_computer_count()
        logging.info(f"New computer count: {new_count}")
        assert new_count > original_computer_count

    def test_cancel_create_computer(self):
        """
        Fills out create computer fields, but cancels the creation. No computer is actually created.
        This corresponds to testcase C2 in the manual test plan
        """
        self.ui.home_page.open_page()
        self.ui.home_page.click_add_computer()
        logging.info("New computer should not be created since cancel button is pressed")
        self.ui.computer_page.create_computer(name="cancel", cancel=True)
        assert len(self.ui.driver.find_elements_by_xpath(HomePageLocators.banner)) == 0

    def test_create_computer_missing_name(self):
        """
        Attempts to create a computer without filling in the name param. This should fail.
        This corresponds to testcase C3 in the manual test plan.
        """
        self.ui.home_page.open_page()
        self.ui.home_page.click_add_computer()
        logging.info("New computer should not be created since it is missing a computer name")
        today = datetime.today().strftime('%Y-%m-%d')
        self.ui.computer_page.create_computer(discontinued_date=today)
        assert self.ui.driver.find_element_by_xpath(ComputerPageLocators.error_alert).is_displayed()


## ----READ---- ###
    @pytest.mark.skipif("TestCRUD.creation_failure")
    def test_search_for_created_computer_full_name(self):
        """
        Searches for computer created previously. Verifies one result is found.
        This corresponds to testcase R1 in the manual test plan
        """
        logging.info(f"Searching for computer: {self.computer_name}")
        self.ui.home_page.open_page()
        self.ui.home_page.search_for_computer(self.computer_name)
        pagination_count = self.ui.home_page.get_pagination_count()
        assert pagination_count == 1
        computers_found_text = self.ui.home_page.get_computer_count()
        assert computers_found_text == "One"
        search_data = self.ui.home_page.get_search_result_info()
        logging.info(f"Grabbed search result: {search_data}")
        self.__class__.computer_link = search_data["href"]
        assert search_data["name"] == self.computer_name

    def test_search_for_created_computers_partial_name(self):
        """
        Searches for computer with substring. Verifes multiple results appear.
        This corresponds to testcase R2 in the manual test plan
        """

        logging.info(f"Searching for computer with terms: AS")
        self.ui.home_page.search_for_computer("AS")
        pagination_count = self.ui.home_page.get_pagination_count()
        assert pagination_count > 1
        computers_found_text = self.ui.home_page.get_computer_count()
        assert computers_found_text > 1

    def test_search_for_nonexistent_name(self):
        """
        Searches for nonexistent computer name. Verifies no results appear.
        This corresponds to testcase R3 in the manual test plan
        """
        nonexist = "123asdfj3i23838383sdjdjdjdj333"
        logging.info(f"Searching for computer with terms: {nonexist}")
        self.ui.home_page.search_for_computer(nonexist)
        computers_found_text = self.ui.home_page.get_computer_count()
        assert computers_found_text == None
        assert self.ui.driver.find_element_by_xpath(HomePageLocators.nothing_to_display).is_displayed()

### ----UPDATE---- ###
    @pytest.mark.skipif("TestCRUD.creation_failure")
    def test_edit_computer_fields(self):
        """
        Updates the company name, introduced date, discontinued date, and company for the previously created computer.
        Verifies the edits apply when searching for the computer.
        This covers testcases U1, U2, U3, and U4 from the manual test plan
        """
        self.ui.driver.get(self.__class__.computer_link)
        edited_name = self.computer_name + "_edited"
        self.__class__.edited_computer_name = edited_name
        yesterday = datetime.today() - timedelta(days=1)
        formatted_yesterday = datetime.strftime(yesterday, '%Y-%m-%d')
        past = datetime.today() - timedelta(days=5)
        formatted_past = datetime.strftime(past, '%Y-%m-%d' )
        company = "OQO"
        self.ui.computer_page.edit_computer(name=edited_name, introduced_date=formatted_past, discontinued_date=formatted_yesterday, company=company)
        WebDriverWait(self.ui.driver, 5).until(
            EC.visibility_of_element_located((By.ID, HomePageLocators.add_button))
        )
        assert "has been updated" in self.ui.driver.find_element_by_xpath(HomePageLocators.banner).text

        logging.info(f"Verify the fields are updated by searching for the edited name: {edited_name}")
        self.ui.home_page.search_for_computer(edited_name)
        pagination_count = self.ui.home_page.get_pagination_count()
        assert pagination_count == 1
        search_data = self.ui.home_page.get_search_result_info()
        assert search_data["name"] == edited_name
        #need extra formatting due to different display dates. I mentioned this in testcase C6
        formatted_introduced_date = datetime.strptime(search_data["introduced_date"], '%d %b %Y').strftime('%Y-%m-%d')
        formatted_discontinued_date = datetime.strptime(search_data["discontinued_date"], '%d %b %Y').strftime('%Y-%m-%d')
        assert formatted_introduced_date == formatted_past
        assert formatted_discontinued_date == formatted_yesterday
        assert search_data["company"] == company

### ----DELETE---- ###
    @pytest.mark.skipif("TestCRUD.creation_failure")
    def test_delete_existing_computer(self):
        """
        Searches for and deletes an existing computer.
        Verifies searching for the deleted computer returns no results.
        This corresponds to testcases R7 and D1 in the manual test plan
        """
        self.ui.home_page.search_for_computer(self.__class__.edited_computer_name)
        logging.info(f"Deleting computer {self.__class__.edited_computer_name}")
        self.ui.driver.get(self.__class__.computer_link)

        self.ui.computer_page.delete_computer()
        WebDriverWait(self.ui.driver, 5).until(
            EC.visibility_of_element_located((By.ID, HomePageLocators.add_button))
        )
        assert "has been deleted" in self.ui.driver.find_element_by_xpath(HomePageLocators.banner).text

        logging.info("Searching for computer to verify it does not appear as a result")
        self.ui.home_page.search_for_computer(self.__class__.edited_computer_name)
        computers_found_text = self.ui.home_page.get_computer_count()
        assert computers_found_text == None
        assert self.ui.driver.find_element_by_xpath(HomePageLocators.nothing_to_display).is_displayed()

    def test_create_delete_computer_rest(self):
        """
        Creates and Deletes a computer via REST calls.
        Uses search to verify creation/deletion.
        This corresponds to testcases C7 and D2 in the manual test plan
        """
        computer_name = self.computer_name + '_rest'
        logging.info(f"Creating computer {computer_name} via REST")
        self.backend.create_computer_rest(f"name={computer_name}&introduced=2021-09-10&discontinued=2021-9-12&company=5")
        time.sleep(3)
        logging.info("Searching for computer to verify creation in UI")
        self.ui.home_page.open_page()
        self.ui.home_page.search_for_computer(computer_name)
        computers_found = self.ui.home_page.get_computer_count()
        assert computers_found == "One"
        search_data = self.ui.home_page.get_search_result_info()
        logging.info(f"Grabbed search result: {search_data}")
        assert search_data["name"] == computer_name
        # grab computer ID from the href link in the xpath
        href = search_data["href"]
        id = href.split("/")[4]

        logging.info(f"Deleting computer {computer_name} via REST")
        self.backend.delete_computer_rest(id)
        time.sleep(3)
        logging.info("Searching for computer to verify deletion in UI. It should not appear in search.")
        self.ui.home_page.search_for_computer(computer_name)
        computers_found_text = self.ui.home_page.get_computer_count()
        assert computers_found_text == None
        assert self.ui.driver.find_element_by_xpath(HomePageLocators.nothing_to_display).is_displayed()




