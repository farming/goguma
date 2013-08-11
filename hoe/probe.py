from bs4 import BeautifulSoup
from urlparse import urlparse, urljoin
import urllib2

class Probe:
    def open(self, url):
        file = urllib2.urlopen(url)
        self.soup = BeautifulSoup(file)
        self.url = url

    def get_internal_url(self, root_page_url):
        url_list = []
        for atag in self.soup.find_all('a'):
            a_link = atag['href']
            if (not self.check_internal_url(root_page_url, a_link)):
                continue

            internal_full_path = urljoin(self.url, a_link)
            url_list.append(internal_full_path)

        return url_list

    def check_internal_url(self, root_page_url, url):
        root_page_url_parsed = urlparse(root_page_url)
        url_parsed = urlparse(url)

        root_page_netloc = root_page_url_parsed.netloc
        page_netloc = url_parsed.netloc
        if (not self.check_netloc(root_page_netloc, page_netloc)):
            return False

        root_page_path = root_page_url_parsed.path
        path = url_parsed.path

        if (path.find(root_page_path) == 0):
            return True

        return False

    def check_netloc(self, root_page_netloc, netloc):
        if root_page_netloc == netloc:
            return True

        if netloc == '':
            return True

        return False
