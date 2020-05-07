# coding:utf-8
from baike_spider.HtmDownload import HtmDownload
from baike_spider.HtmOutput import HtmOutput
from baike_spider.HtmParser import HtmParser
from baike_spider.UrlManager import UrlManager


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
                print("new_urls size = %d" % len(new_urls))
                counter += 1
            except Exception as e:
                print("html parse error !!", e)
            if counter > 5:
                self.htm_output.save()
                break


if __name__ == '__main__':
    # 保定词条
    # root_url = "https://baike.baidu.com/item/%E4%BF%9D%E5%AE%9A/84913?fr=aladdin"
    # 二战词条
    root_url = "https://baike.baidu.com/item/%E7%AC%AC%E4%BA%8C%E6%AC%A1%E4%B8%96%E7%95%8C%E5%A4%A7%E6%88%98/174090?fr=aladdin#2"
    spider = SpiderMain()
    spider.run(root_url)
