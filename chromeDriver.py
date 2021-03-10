from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
driver.get('https://oakhillcc.com/group/pages/member-roster')
buttons = driver.find_element_by_xpath("//*[contains(text(), 'Member Roster')]")
buttons.click()
# time.sleep(5)
pageBtn = driver.find_element_by_xpath("//*[contains(text(), '2')]")
pageBtn.click()



