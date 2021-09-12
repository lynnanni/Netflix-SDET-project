import logging


class Page:
    def __init__(self, driver, name, url):
        self.driver = driver
        self.name = name
        self.url = url

    def open_page(self):
        logging.info(f"Opening page: {self.url}")
        self.driver.get(self.url)