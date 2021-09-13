# Readme
- [Project Description](#project-description)
- [Test Setup](#test-setup)
  * [Assumptions](#assumptions)
  * [Steps](#steps)
    + [Troubleshooting](#troubleshooting)
- [Tests Automated](#tests-automated)
- [Test Framework Overview](#test-framework-overview)
- [TODO](#todo)



## Project Description
This project automates some of the test cases written in Anni-NetflixTestPlan.numbers using Pytest and Selenium. 

## Test Setup

### Assumptions
- User is running the tests on a Mac-like system
- Python 3.6 or later is installed.
- Chrome is installed

### Steps
First, install requirements.txt:

`pip3 install -r requirements.txt`


Second, you will also need to download the `chromedriver` version that matches your current chrome browser's.

https://www.swtestacademy.com/install-chrome-driver-on-mac

To run the tests from the CLI, run this command: 

`pytest -v Testcases/CRUD.py`

Or, import the project into an IDE such as Pycharm and edit the run configuration to select Python tests. You can select the test you would like to run based off the script path. 

Example: `/Users/anniwang/PycharmProjects/anni_netflix_project/Testcases/CRUD.py`

#### Troubleshooting

If you encounter issues with chromedriver, you may need to run these commands:

`sudo chmod a+x /usr/local/bin/chromedriver` (permissions)

`xattr -d com.apple.quarantine /usr/local/bin/chromedriver` (mac security update)

## Tests Automated
- Add a new computer - happy path
- Add a new computer - cancel
- Add a new computer - missing name  
- Search for an existing computer - full name
- Search for an existing computer - substring
- Search for a nonexistent computer 
- Edit computer name, introduced date, discontinued date, company
- Delete existing computer
- Create and Delete computer via REST

## Test Framework Overview
- "CRUD.py" lives in the Testcases folder. This contains all of the automated End-to-End tests.
- Modules/Library contains Backend.py, which represents some of the REST APIs such as create computer/delete computer.
- Frontend.py instantiates the web browser as well as creating pages to take actions on.
- Locators.py contains xpaths and ids used by Selenium to find objects to interact with, such as buttons to click or textboxes to type in.
- Modules/Pages contains the "Page Object Model" pages that represent different user interfaces.
- To see sample test results, please view `sample-run-output.txt` and `pytest_run_example.png` 


## TODO 
With more time to work on this, I would add: 
- Screenshot capture function. When the tests run in an automation pipeline, we could review screenshots to verify the test is behaving correctly.
- More browser coverage (Firefox, Safari, etc)
- Flesh out backend related tests in Backend.py
- Remove some test dependencies by creating the preconditions in the test setup. Currently all the tests run in the single CRUD.py file. I could split them up into different test files that run independently.
- Organize locators.py better. It looks a bit messy right now. 
