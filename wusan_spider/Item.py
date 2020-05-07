# -*- coding: utf-8 -*-
# ==========================================
# Author : mk
# Create Time : 2020/5/7 - 13:13
# File Name : Item.py
# Description : 
# Software: PyCharm
# ==========================================


class Layer:
    def __init__(self):
        self.data = dict()
        self._labels = None

    def _add(self, key='ROOT', data=None):
        self.data[key] = data

    def set_labels(self, key='ROOT', labels=None):
        self._labels = labels
        if labels is None:
            return
        data = []
        for label in labels:
            data.append(label.text)
        self._add(key=key, data=data)

    def get_labels(self, key=None):
        if key is None:
            return self._labels
        else:
            return self.data.get(key)

    def __str__(self):
        return self.data.__str__()


class Layer1(Layer):
    pass


class Layer2(Layer):
    pass


class Layer3(Layer):

    def __init__(self):
        super(Layer3, self).__init__()
        # 第三层数据
        self.data3 = list()
        # 包含第二层目录
        self.data2 = dict()

    def set_labels(self, key='ROOT', labels=None):
        self._labels = labels
        if labels is None:
            return
        data = []
        for label in labels:
            data.append(label.text)
        self._add(key=key, data=data)
        self.data3.append(self.data)

    def set_p_key(self, p_key):
        self.data2[p_key] = self.data3

    def get_by_p_key(self, p_key):
        return self.data2.get(p_key)

    def __str__(self):
        return self.data2.__str__()


class Layer4(Layer):
    pass


class Layer5(Layer):
    pass


class Tree:
    """
    树形结构体，分为四级
    1、年份(2020版)
    2、课标(课标I)
    3、科目(语文)
    4、专题(专题一 论述类文本阅读)
    5、资料
    """

    def __init__(self):
        self.layer1 = Layer1()
        self.layer2 = Layer2()
        self.layer3 = Layer3()
        self.layer4 = Layer4()
        self.layer5 = Layer5()

    def __str__(self):
        return self.layer1.__str__() + "\n" + self.layer2.__str__() + "\n" + self.layer3.__str__() + "\n" + self.layer4.__str__() + "\n" + self.layer5.__str__()
