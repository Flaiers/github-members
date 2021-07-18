
# importing libraries
import requests
from time import sleep
from dbActions import dbSaver
from prettytable import PrettyTable
from bs4 import BeautifulSoup as bs


# class for parsing and generate table
class GenerateTable:

    # A function that initially writes parameters to the self.table
    # variable is set self.page equal to page number, and get link
    def __init__(self, company):
        self.link = 'https://github.com/'
        self.company = company
        self.page = 1
        self.number = 1
        self.table = PrettyTable()
        self.table.field_names = ['№', 'Name', 'Username', 'Followers', 'Following', 'Stars', 'Location',
                                'Repositories', 'Contributions', 'Profile link']

    # A function that parses data from the my GitHub account 
    # and sets new rows in the table
    def getMyData(self):
        myUsername = 'Flaiers'
        myProfile_link = self.link + myUsername
        page_founder = requests.get(myProfile_link)
        html_founder = bs(page_founder.content, 'html.parser')

        myName = html_founder.find('span', class_='p-name').text.strip()
        myDescription = html_founder.find('div', class_='p-note')
        myDescription = myDescription.text.replace('\n', '') if myDescription is not None else ''

        myInfo = html_founder.find_all('span', class_='text-bold')
        myFollowers = myInfo[0].text
        myFollowing = myInfo[1].text
        myStars = myInfo[2].text

        myLocation = html_founder.find('span', class_='p-label')
        myLocation = myLocation.text if myLocation is not None else ''

        myRepositories = html_founder.find('span', class_='Counter').text
        myContributions = html_founder.find('h2', class_='f4 text-normal mb-2').text.strip().split('\n')[0]

        self.table.add_row([str(self.number), myName, myUsername, myFollowers, myFollowing, myStars, 
                            myLocation, myRepositories, myContributions, myProfile_link])
        db = dbSaver(myName, myUsername, myDescription, myFollowers, myFollowing, myStars, myLocation,
                    myRepositories, myContributions, myProfile_link)
        db.save()

        self.getData()

    # A function that parses data from the GitHub and sets new rows 
    # in the table, looping through the pages
    def getData(self):

        # The same loop that iterates through the pages
        # If the pages end, the loop is terminated by calling break
        while 1:
            page_of_members = requests.get(f'{self.link}orgs/{self.company}/people?page={self.page}')
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

                    self.table.add_row([str(self.number), name, username, followers, following, stars, location,
                                        repositories, contributions, profile_link])
                    db = dbSaver(name, username, description, followers, following, stars, location, repositories,
                                contributions, profile_link)
                    db.save()
                    sleep(1)

                self.page += 1

            # The page does not exist
            else:
                break
