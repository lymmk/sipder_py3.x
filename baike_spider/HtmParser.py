from bs4 import BeautifulSoup
import re
import urlparse


class HtmParser:
    def __init__(self):
        pass

    def parse(self, new_url, htm_file):
        if new_url == None or htm_file == None:
            return None
        soup = BeautifulSoup(htm_file, features='html.parser', from_encoding="utf-8")
        new_urls = self._get_new_urls(new_url, soup)
        new_data = self._get_new_data(new_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, new_url, soup):
        new_urls = set()
        # href="/item/%E7%9B%B4%E9%9A%B6%E6%80%BB%E7%9D%A3/3494828"
        urls = soup.find_all('a', href=re.compile("/item/?"))
        for url in urls:
            link = urlparse.urljoin(new_url, url['href'])
            new_urls.add(link)
        return new_urls


    def _get_new_data(self, new_url, soup):
        res_data = {}
        res_data['url'] = new_url
        data_title = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = data_title.get_text()

        data_summary = soup.find('div', class_="lemma-summary")
        res_data['summary'] = data_summary.get_text()
        return res_data