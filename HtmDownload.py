import urllib2


class HtmDownload:
    def __init__(self):
        pass

    def download(self, url):
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
