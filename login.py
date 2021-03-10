from bs4 import BeautifulSoup
import requests
from selenium import webdriver

# Start the session
session = requests.Session()

# Create the payload
# noinspection SpellCheckingInspection
payload = {'_58_login':'[2987]',
          '_58_password': '[Pinboy1$]'
         }

# Post the payload to the site to log in
s = session.post('https://oakhillcc.com/web/pages/login?p_p_id=58&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=1&_58_struts_action=%2Flogin%2Flogin')

# Navigate to the next page and scrape the data
s = session.get('https://oakhillcc.com/group/pages/home')
print(s)
soup = BeautifulSoup(s.text, 'lxml')
print(soup.prettify())
# print(soup.find('title').text)