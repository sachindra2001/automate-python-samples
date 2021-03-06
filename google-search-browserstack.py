import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

try:
    USERNAME = sys.argv[1]
    BROWSERSTACK_KEY = sys.argv[2]
except IndexError:
    print("Pleaes provide the username and browserstack access key as command line arguments.")
    sys.exit(1)

driver = webdriver.Remote(
    command_executor='http://%s:%s@hub.browserstack.com/wd/hub' %(
        USERNAME, BROWSERSTACK_KEY
    ),
    desired_capabilities=DesiredCapabilities.FIREFOX
)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")

elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.submit()

print driver.title
driver.quit()
