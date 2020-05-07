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

    def _add(self, p_layer='TOP', data=None):
        self.data['parent_layer'] = p_layer
        self.data['data'] = data
        pass

    def set_labels(self, p_layer='TOP', labels=None):
        self._labels = labels
        if labels is None:
            return
        data = []
        for label in labels:
            data.append(label.text)
        self._add(p_layer=p_layer, data=data)

    def get_labels(self):
        return self._labels

    def __str__(self):
        return self.data.__str__()


class Layer1(Layer):
    pass


class Layer2(Layer):
    pass


class Layer3(Layer):
    pass


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
