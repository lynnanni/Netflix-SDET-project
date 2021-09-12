from Modules.Pages.BasePage import Page
from Modules.Library.locators import HomePageLocators as locators

class HomePage(Page):
    """
    This is the main URL you visit to test: http://computer-database.herokuapp.com/computers
    """

    def __init__(self, driver, url="http://computer-database.herokuapp.com/computers"):
        super(HomePage, self).__init__(driver, "home_page", url=url)

    def click_add_computer(self):
        """ Clicks the green 'Add a new computer' button """
        element = self.driver.find_element_by_id(locators.add_button)
        element.click()

    def search_for_computer(self, search_string):
        """
        :param search_string: the name of the computer you are searching for
        Types in the name search_string and presses the "Filter by name" button
        """
        search_box = self.driver.find_element_by_id(locators.search_box)
        search_box.clear()
        search_box.send_keys(search_string)
        self.driver.find_element_by_id(locators.search_button).click()

    def get_computer_count(self):
        """
        Returns the amount of computers currently in the database by checking the text on top of the home page.
        """
        count_phrase = self.driver.find_element_by_xpath(locators.computers_found).text
        try:
            count = int(count_phrase.split()[0])
        except ValueError:
            if count_phrase == "No computers found":
                count = None
            else:
                # only one computer found = no numbers will be shown. UI will show "One computer found"
                count = "One"
        return count

    def get_pagination_count(self):
        """
        Returns the total number of search results from the bottom pagination
        Example: Displaying 1 to 10 of 25
        This would return the number 25
        """
        count_phrase = self.driver.find_element_by_xpath(locators.current_pagination).text
        return int(count_phrase.split()[5])

    def get_search_result_info(self):
        """
        Grabs the href link data and name of the search result
        :return: returns a dictionary with search result items
        """
        result = {}
        href = self.driver.find_element_by_xpath(locators.search_result_computer_name).get_attribute('href')
        name = self.driver.find_element_by_xpath(locators.search_result_computer_name).text
        introduced_date = self.driver.find_element_by_xpath(locators.search_result_introduced_date).text
        discontinued_date = self.driver.find_element_by_xpath(locators.search_result_discontinued_date).text
        company = self.driver.find_element_by_xpath(locators.search_result_company).text
        result["href"] = href
        result["name"] = name
        result["introduced_date"] = introduced_date
        result["discontinued_date"] = discontinued_date
        result["company"] = company
        return result