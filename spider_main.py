from HtmDownload import HtmDownload
from HtmOutput import HtmOutput
from HtmParser import HtmParser
from UrlManager import UrlManager


class SpiderMain:
    def __init__(self):
        self.url_manager = UrlManager()
        self.htm_download = HtmDownload()
        self.htm_parser = HtmParser()
        self.htm_output = HtmOutput()

    def run(self, url):
        self.url_manager.add_new_url(url)
        counter = 1
        while self.url_manager.has_new_url():
            try:
                new_url = self.url_manager.get_new_url()
                htm_cont = self.htm_download.download(new_url)
                new_urls, htm_data = self.htm_parser.parse(new_url, htm_cont)
                self.url_manager.add_new_urls(new_urls)
                self.htm_output.append(htm_data)
                print("%d html parsed , url = %s" % (counter, new_url))
                counter += 1
            except:
                print ("html pars error !!")
            if counter > 5:
                self.htm_output.save()
                break


if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/%E4%BF%9D%E5%AE%9A/84913?fr=aladdin"
    spider = SpiderMain()
    spider.run(root_url)
