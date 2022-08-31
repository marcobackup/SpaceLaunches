import aifc
import requests
from bs4 import BeautifulSoup
import re


class LaunchesScraper:

    def __init__(self):
        self.apiEndpoint = 'https://go4liftoff.com/'
        self.websiteUrl  = f'{self.apiEndpoint}launches?item_count=5'

    def getLaunches(self):
        launches = []
        res = requests.get(self.websiteUrl)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            for launch in soup.find_all('div', {'class': 'd-flex launchHeader'}):
                launch = launch.find_parent(
                                    'div', 
                                    {'class': 'card-body'}
                                ).find(
                                    'div', 
                                    {'class': 'spaceEvenly'}
                                ).findChildren('div')
                launches.append(launch[2].find('a').get('href'))
            return launches
        else:
            return False

    def getLaunchesDetails(self):
        launchesDetails = {}
        for launchUrl in self.getLaunches():
            res = requests.get(f'{self.apiEndpoint}{launchUrl}', timeout=(3.05, 27))
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                cards = soup.find_all('div', {'class': 'card'})
                launchesDetails['mission'] = {
                    'name': cards[0].find('h3', {'class': 'card-title'}).text.split('|')[1].replace(' ', ''),
                    'launchSite': cards[0].find('div', {'class': 'card-text'}).findChildren('h6')[0].text.replace(' ', ''),
                    'place': cards[0].find('div', {'class': 'card-text'}).findChildren('h6')[1].text,
                    'date': cards[0].find('h5', {'id': re.compile('date-[A-z-0-9$?]*')}).text
                }
            else:
                return False;
            break
        return launchesDetails

