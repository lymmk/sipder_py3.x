# coding:utf-8
from img_spider.ImgDownloader import ImgDownloader
from img_spider.ImgPathManager import ImgPathManager
from img_spider.UrlManager import UrlManager
from img_spider.UrlParser import UrlParser
import time


class ImgSpider:
    error_paths = set()

    def __init__(self, _url):
        self.url_manager = UrlManager()
        self.img_downloader = ImgDownloader()
        self.img_path_manager = ImgPathManager()
        self.url_parser = UrlParser()
        self.img_paths = self.__get_img_paths(_url)

    def __get_img_paths(self, _url):
        # self.url_manager.addUrl(_url)
        html_file = self.url_parser.download_html(_url)
        return self.url_parser.parse_html(html_file)

    def run(self):
        count = 0
        for path in self.img_paths:
            # noinspection PyBroadException
            try:
                count += 1
                print ("path = %s" % path)
                self.img_downloader.download(path)
                print ("Downloaded image %d/%d" % (count, len(self.img_paths)))
            except Exception:
                print ("Download error image %d/%d url:%s " % (count, len(self.img_paths), path))
                # print(Arguments)
                # 记录下载失败项
                if str(path).endswith("jpg"):
                    self.error_paths.add(path)
        time.sleep(1)
        print ("Download Done %d files!!" % (count-len(self.error_paths)))


if __name__ == "__main__":
    # url = sys.argv[0]
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4516913.html"
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4500380.html"
    url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4500345.html"
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4498299.html"
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4498297.html"
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4498293.html"
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4498285.html"
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4498278.html"
    spider = ImgSpider(url)
    spider.run()
    while len(spider.error_paths) != 0:
        spider.img_paths = spider.error_paths
        spider.error_paths = set()
        spider.run()
