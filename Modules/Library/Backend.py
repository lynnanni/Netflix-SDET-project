import requests

class Backend:

    def __init__(self):
        pass

    def delete_computer_rest(self, computer_id):
        if not computer_id:
            return "Please include a computer_id to be deleted"
        requests.post(f"http://computer-database.herokuapp.com/computers/{computer_id}/delete")

    def create_computer_rest(self, params=""):
        """
        :param params: Should be formatted like this: name=asdf&introduced=2021-09-11&discontinued=2021-9-12&company=3
        You will need to know the company ID
        """
        requests.post("http://computer-database.herokuapp.com/computers", params=params)