from bs4 import BeautifulSoup
import requests


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    emailCheck = '@'
    nameCount = 0
    emailCount = 0
    with open('Member Roster - Oak Hill Country Club.html') as source:

    # source = requests.get('https://oakhillcc.com/group/pages/member-roster').text
        # soup = BeautifulSoup(source, 'lxml')
        soup = BeautifulSoup(source, 'lxml')
    # print(soup.prettify())

    # names = soup.find_all('span', class_='roster-member-name').text
    # print(names)
    #
    for memberName in soup.find_all('span', class_='roster-member-name'):
        nameCount = nameCount + 1
        print(str(nameCount) + ': ' + memberName.text)
    # for memberEmail in soup.find_all('a', class_='roster-normal-link'):
    #     memberEmail = memberEmail.text
    #     if emailCheck in memberEmail:
    #         emailCount = emailCount + 1
    #         # print(str(emailCount) + ': ' + memberEmail)
    #
    #
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
