# Readme

## Project Description
This project automates some of the manual tests written in Anni-NetflixTestPlan. 

## Test Setup
To run the tests, please load the project in an IDE such as Pycharm. Edit the run configuration to select Python tests. Finally, select the test you would like to run based off the script path. 

Example: `/Users/anniwang/PycharmProjects/anni_netflix_project/Testcases/CRUD.py`


To see the tests run in the UI, please install the chromedriver version that matches your chrome browser's.

https://www.swtestacademy.com/install-chrome-driver-on-mac

Also install requirements.txt:

`pip3 install -r requirements.txt`

### Troubleshooting

If you encounter issues with chromedriver, you may need to run these commands:

`sudo chmod a+x /usr/local/bin/chromedriver`

`xattr -d com.apple.quarantine /usr/local/bin/chromedriver
`
## Still TODO 
With more time to work on this, I would add: 
- Screenshot capture function. When the tests run in an automation pipeline, we could review screenshots to verify the test is behaving correctly.
- More browser coverage (Firefox, Safari, etc)
- Backend related test coverage with REST API checking (Backend.py)
- Remove some of the test dependencies by creating the preconditions in the test setup. Currently all the tests run in the single CRUD.py file. I could split them up into different test files that run independently.
