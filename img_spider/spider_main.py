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
                self.img_downloader.download(path)
                count += 1
                print ("Downloading image %d/%d" % (count, len(img_paths)))
            except Exception:
                # count += 1
                print ("Download error image %d/%d url:%s " % (count, len(img_paths), path))
            # count += 1
        print ("Download Done %d files!!" % count)


if __name__ == "__main__":
    url = "http://q1.fnmdsbb.club/pw/html_data/14/1908/4272820.html"
    # url = "http://q1.fnmdsbb.club/pw/html_data/14/1908/4272821.html"
    # url = "http://q1.fnmdsbb.club/pw/html_data/14/1908/4272823.html"
    spider = ImgSpider()
    spider.run(url)
