# coding:utf-8
from wusan_spider.HtmDownload import HtmDownload
from wusan_spider.HtmOutput import HtmOutput
from wusan_spider.HtmParser import HtmParser
from wusan_spider.UrlManager import UrlManager
from wusan_spider.CustomSelenium import BrowserDriver
from wusan_spider.Item import *
import time


class SpiderMain:
    def __init__(self):
        self.htm_download = HtmDownload()
        self.htm_parser = HtmParser()
        self.htm_output = HtmOutput()
        self.driver = BrowserDriver()
        self.tree_item = Tree()

    def run(self, url):
        self.driver.open(url)
        labels = self.driver.browser.find_elements_by_tag_name('label')
        self.htm_parser.set_labels(labels)
        self.tree_item.layer1.set_labels(labels=self.htm_parser.parse_layer1())
        for label in self.tree_item.layer1.get_labels():
            print(label.text)
            label.click()
            # 等待加载1秒
            time.sleep(1)
            self.tree_item.layer2.set_labels(p_layer=label.text, labels=self.htm_parser.parse_layer2())
        print(self.tree_item)
        self._stop()

    def _stop(self):
        self.driver.close()


if __name__ == '__main__':
    # 新 53 B版
    root_url = "http://zy.quyixian.com/NewFiveThreeB/"
    spider = SpiderMain()
    spider.run(root_url)
