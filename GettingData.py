
# importing libraries
import requests
from time import sleep
from prettytable import PrettyTable
from bs4 import BeautifulSoup as bs


# class for parsing and generate table
class GenerateTable:

    # A function that initially writes parameters to the self.table
    # variable is set self.page equal to page number, and get link
    def __init__(self, link):
        self.link = link
        self.page = 1
        self.number = 1
        self.table = PrettyTable()
        self.table.field_names = ['№', 'Name', 'Username', 'Description', 'Followers', 'Following', 'Stars', 'Location', 'Repositories', 'Contributions', 'Profile link']
        self.table.add_row(['1', 'Maxim Bigin', 'Flaiers', 'Python Junior Developer', '9', '9', '47', 'Moscow', '30', '380', 'https://github.com/Flaiers'])

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
            if len(members):
                for member in members:
                    member = member.find('a', class_='css-truncate-target')
                    self.number += 1
                    name = member.text.strip()
                    username = member.get('href').replace('/', '')
                    profile_link = self.link + username

                    page_profile = requests.get(profile_link)
                    html_profile = bs(page_profile.content, 'html.parser')
                    description = html_profile.find('div', class_='p-note')
                    description = description.text.replace('\n', '') if description is not None else ''

                    info = html_profile.find_all('span', class_='text-bold')
                    followers = info[0].text
                    following = info[1].text
                    stars = info[2].text

                    location = html_profile.find('span', class_='p-label')
                    location = location.text if location is not None else ''

                    repositories = html_profile.find('span', class_='Counter').text
                    contributions = html_profile.find('h2', class_='f4 text-normal mb-2').text.strip().split('\n')[0]

                    self.table.add_row([str(self.number), name, username, description, followers, following, stars, location, repositories, contributions, profile_link])
                    sleep(2)

                self.page += 1

            # The page does not exist
            else:
                break
