class HomePageLocators:
    """
    All home page locators should be stored here
    """
    add_button = "add" #id
    search_box = "searchbox" #id
    search_button = "searchsubmit" #id
    next_button = "//*[text()='Next →']" #xpath
    banner = "//*[@class='alert-message warning']" #xpath
    computers_found = "//h1[contains(text(), 'found')]" #xpath
    current_pagination = "//*[@class='current']" #xpath
    search_result_computer_name = "//*[@class='computers zebra-striped']//td/a" #xpath
    search_result_introduced_date = "//tbody//td[2]" #xpath
    search_result_discontinued_date = "//tbody//td[3]" #xpath
    search_result_company = "//tbody//td[4]" #xpath
    nothing_to_display = "//em" #xpath

class ComputerPageLocators:
    """
    Add a new computer page locators stored here
    """
    computer_name = "name" #id
    introduced_date = "introduced" #id
    discontinued_date = "discontinued" #id
    company = "company" #id
    create_computer_button = "//*[@value='Create this computer']" #xpath
    cancel_button = "//*[@class='btn' and text()='Cancel']" #xpath
    save_computer_button = "//*[@value='Save this computer']" #xpath
    delete_computer_button = "//*[@value='Delete this computer']" #xpath