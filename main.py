import config
import requests
from bs4 import BeautifulSoup as bs


def get_data(link):
    while 1:
        page_of_members = requests.get(f'{link}?page={config.page_number}')
        html_of_members = bs(page_of_members.content, 'html.parser')
        members = html_of_members.find_all("li", class_="table-list-item")

        if (len(members)):
            for member in members:
                member = member.find('a', class_='css-truncate-target')
                name = member.text.strip()
                username = member.get('href').replace('/', '')
                link = f"https://github.com/{username}"
                print(name, username, link)

            config.page_number += 1
        else:
            break


if __name__ == '__main__':
    get_data('https://github.com/orgs/github/people')
