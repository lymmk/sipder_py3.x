# coding:utf-8
from img_spider.ImgDownloader import ImgDownloader
from img_spider.ImgPathManager import ImgPathManager
from img_spider.UrlManager import UrlManager
from img_spider.UrlParser import UrlParser


class ImgSpider:
    def __init__(self):
        self.url_manager = UrlManager()
        self.img_downloader = ImgDownloader()
        self.img_path_manager = ImgPathManager()
        self.url_parser = UrlParser()

    def run(self, _url):
        # self.url_manager.addUrl(_url)
        html_file = self.url_parser.download_html(_url)
        img_paths = self.url_parser.parse_html(html_file)
        # self.img_path_manager.addPaths(img_paths)
        count = 0
        for path in img_paths:
            # noinspection PyBroadException
            try:
                count += 1
                print ("path = %s" % path)
                self.img_downloader.download(path)
                print ("Downloaded image %d/%d" % (count, len(img_paths)))
            except Exception:
                print ("Download error image %d/%d url:%s " % (count, len(img_paths), path))
        print ("Download Done %d files!!" % count)


if __name__ == "__main__":
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4500380.html"
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4500345.html"
    url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4498299.html"
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4498297.html"
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4498293.html"
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4498285.html"
    # url = "http://x1.sjlxmwpb79.rocks/pw/html_data/14/1912/4498278.html"
    spider = ImgSpider()
    spider.run(url)
