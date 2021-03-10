from bs4 import BeautifulSoup
import requests

# Start the session
session = requests.Session()

# Create the payload
payload = {'_username':'[aburito97]',
          '_password':'[Fatass_1997]'
         }

# Post the payload to the site to log in
s = session.post("https://www.chess.com/login_check", data=payload)

# Navigate to the next page and scrape the data
s = session.get('https://www.chess.com/today')

soup = BeautifulSoup(s.text, 'html.parser')
print(soup.find('title').text)
