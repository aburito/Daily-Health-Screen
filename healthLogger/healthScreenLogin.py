from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import sys


#########################################################
#   Make sure you change the path download link below   #
#           https://chromedriver.chromium.org/          #
#########################################################
def DailyHealthLogger(userName, passWord):
    driver = webdriver.Chrome(executable_path="C:/Users/drdst/chromedriver.exe")
    driver.maximize_window()

    driver.get("https://dailyhealth.rit.edu")
    time.sleep(3)
    username = driver.find_element_by_id("username")
    username.send_keys(userName)
    password = driver.find_element_by_id('password')
    password.send_keys(passWord)
    password.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.get('https://dailyhealth.rit.edu/assessment')
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div')
    action = ActionChains(driver)
    action.click(on_element=element)
    action.perform()
    time.sleep(5)
    driver.close()


DailyHealthLogger(sys.argv[1], sys.argv[2])
