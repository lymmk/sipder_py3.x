# coding:utf-8
import re
import urllib.request as urllib2
from bs4 import BeautifulSoup


class UrlParser:
    def parse_html(self, html):
        if html == None:
            return None
        soup = BeautifulSoup(html, features='html.parser', from_encoding="utf-8")
        return self._get_img_paths(soup)

    def _get_img_paths(self, soup):
        img_paths = set()
        # href="/item/%E7%9B%B4%E9%9A%B6%E6%80%BB%E7%9D%A3/3494828"
        paths = soup.find_all('img')
        for url in paths:
            link = url['src']
            if str(link).endswith("jpg"):
                img_paths.add(link)
        return img_paths

    def download_html(self, url):
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
        response = urllib2.urlopen(request)
        if response.getcode() != 200:
            return None
        return response.read()
