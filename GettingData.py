
# importing libraries
import requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup as bs


# class for parsing and generate table
class GenerateTable:

    # A function that initially writes parameters to the self.table
    def __init__(self, link):
        self.link = link
        self.page = 1
        self.table = PrettyTable()
        self.table.field_names = ['Name', 'Username', 'Profile link']
        self.table.add_row(['Maxim Bigin', 'Flaiers', 'https://github.com/Flaiers'])

    # A function that parses data from the GitHub and sets new rows 
    # in the table, looping through the pages
    def getData(self):

        # The same loop that iterates through the pages
        # If the pages end, the loop is terminated by calling break
        while 1:
            page_of_members = requests.get(f'{self.link}orgs/github/people?page={self.page}')
            html_of_members = bs(page_of_members.content, 'html.parser')
            members = html_of_members.find_all("li", class_="table-list-item")

            # The page exists
            if (len(members)):
                for member in members:
                    member = member.find('a', class_='css-truncate-target')
                    name = member.text.strip()
                    username = member.get('href').replace('/', '')
                    profile_link = self.link + username
                    self.table.add_row([name, username, profile_link])

                self.page += 1
            
            # The page does not exist
            else:
                break
