from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import sys
from datetime import datetime
import smtplib, ssl

from email.message import EmailMessage
from datetime import date



#########################################################
#   Make sure you change the path download link below   #
#           https://chromedriver.chromium.org/          #
#########################################################
def DailyHealthLogger(userName, passWord):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
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
    Email(userName)

    context = ssl.create_default_context()
def Email(username):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "dailyhealthlogger@gmail.com"  # Enter your address
    receiver_email = username + '@rit.edu'  # Enter receiver address
    password = 'AutomateHealth21'
    message = f"""\
    Subject: Daily Health Complete {datetime.now()}

    Your daily health screen was completed on {datetime.now()}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print('Email Sent')


DailyHealthLogger(sys.argv[1], sys.argv[2])
