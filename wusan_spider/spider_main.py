# coding:utf-8
import time

from wusan_spider.CustomSelenium import BrowserDriver
from wusan_spider.HtmDownload import HtmDownload
from wusan_spider.HtmOutput import HtmOutput
from wusan_spider.HtmParser import HtmParser
from wusan_spider.Item import *


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
        # 获取第二层数据
        self.get_layer2()
        print(self.tree_item)
        self.htm_output.save_to_xmind(self.tree_item)
        self._stop()

    def get_layer2(self):
        for label in self.tree_item.layer1.get_labels():
            # 刷新页面元素
            label.click()
            labels = self.driver.browser.find_elements_by_tag_name('label')
            self.htm_parser.set_labels(labels)
            # 等待加载1秒
            time.sleep(1)
            self.tree_item.layer2.set_labels(key=label.text, labels=self.htm_parser.parse_layer2())
            # 获取第三层数据
            self.get_layer3()
            self.tree_item.layer3.set_p_key(label.text)

    def get_layer3(self):
        for label in self.tree_item.layer2.get_labels():# error
            # 刷新页面元素
            label.click()
            labels = self.driver.browser.find_elements_by_tag_name('label')
            self.htm_parser.set_labels(labels)
            # 等待加载1秒
            time.sleep(1)
            self.tree_item.layer3.set_labels(key=label.text, labels=self.htm_parser.parse_layer3())

    def _stop(self):
        self.driver.close()


if __name__ == '__main__':
    # 新 53 B版
    root_url = "http://zy.quyixian.com/NewFiveThreeB/"
    spider = SpiderMain()
    spider.run(root_url)
