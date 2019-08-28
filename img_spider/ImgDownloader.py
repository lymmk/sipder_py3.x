# coding:utf-8
import urllib2

class ImgDownloader:
    def download(self, url):
        f_name = url[-8:]
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
        f = urllib2.urlopen(request)
        with open("../download/%s" % f_name, "wb") as code:
            code.write(f.read())
