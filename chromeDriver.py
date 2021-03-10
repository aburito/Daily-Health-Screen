from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

######################################
#     Make Sure To Change Path       #
######################################
driver = webdriver.Chrome(executable_path="C:/Users/drdst/chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://oakhillcc.com/web/pages/login")
#to refresh the browser
# driver.refresh()
# identifying the link with the help of link text locator
# driver.find_element_by_link_text("Company").click()
#to close the browser
# driver.close()
inputElement = driver.find_element_by_id("_58_login")
inputElement.send_keys('2987')
inputElement2 = driver.find_element_by_id('_58_password')
inputElement2.send_keys('Pinboy1$')
inputElement2.send_keys(Keys.ENTER)
time.sleep(3)
print('test')
driver.get('https://oakhillcc.com/group/pages/member-roster')
time.sleep(5)
driver.find_element_by_class_name('ui-icon-seek-next')

# buttons = driver.find_element_by_link_text("Member Roster").click()
# time.sleep(3)
# driver.refresh()
# time.sleep(3)
# pageBtn = driver.find_element_by_xpath("//*[contains(text(), '2')]")
# pageBtn.click()



