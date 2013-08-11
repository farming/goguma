from bs4 import BeautifulSoup
import urllib2

class Probe:
    def open(self, url):
        file = urllib2.urlopen(url)
        self.soup = BeautifulSoup(file)

    def get_internal_url(self):
        url_list = []
        for atag in self.soup.find_all('a'):
            url = atag['href']
            url_list.append(url)

        return url_list

