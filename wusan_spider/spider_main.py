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
            self.tree_item.layer2.set_labels(key1=label.text, labels=self.htm_parser.parse_layer2())
            # 获取第三层数据
            self.get_layer3(label.text)
        pass

    def get_layer3(self, key1):
        for label in self.tree_item.layer2.get_labels(key1=key1):
            # 刷新页面元素
            label.click()
            labels = self.driver.browser.find_elements_by_tag_name('label')
            self.htm_parser.set_labels(labels)
            # 等待加载1秒
            time.sleep(1)
            self.tree_item.layer3.set_labels(key1=key1, key2=label.text, labels=self.htm_parser.parse_layer3())
            # 获取第四层数据
            self.get_layer4(key1, label.text)
        pass

    def get_layer4(self, key1, key2):
        for label in self.tree_item.layer3.get_labels(key1=key1, key2=key2):
            # 刷新页面元素
            label.click()
            # 等待加载1秒
            time.sleep(1)
            spans = self.driver.browser.find_elements_by_tag_name('span')
            self.htm_parser.set_labels(spans)
            self.tree_item.layer4.set_labels(key1=key1, key2=key2, key3=label.text, labels=self.htm_parser.parse_layer4())
        pass

    def _stop(self):
        self.driver.close()


if __name__ == '__main__':
    # 新 53 B版
    root_url = "http://zy.quyixian.com/NewFiveThreeB/"
    spider = SpiderMain()
    spider.run(root_url)
