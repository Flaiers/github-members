import config
import requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup as bs


class GenerateTable:
    def __init__(self):
        self.table = PrettyTable()
        self.table.field_names = ['Name', 'Username', 'Profile link']
        self.table.add_row(['Maxim Bigin', 'Flaiers', 'https://github.com/Flaiers'])

    def getData(self, link):
        while 1:
            page_of_members = requests.get(f'{link}orgs/github/people?page={config.page_number}')
            html_of_members = bs(page_of_members.content, 'html.parser')
            members = html_of_members.find_all("li", class_="table-list-item")

            if (len(members)):
                for member in members:
                    member = member.find('a', class_='css-truncate-target')
                    name = member.text.strip()
                    username = member.get('href').replace('/', '')
                    profile_link = link + username
                    self.table.add_row([name, username, profile_link])

                config.page_number += 1
            else:
                break


if __name__ == '__main__':
    object = GenerateTable()
    object.getData('https://github.com/')
    print(object.table)
