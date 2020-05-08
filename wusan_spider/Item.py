# -*- coding: utf-8 -*-
# ==========================================
# Author : mk
# Create Time : 2020/5/7 - 13:13
# File Name : Item.py
# Description : 
# Software: PyCharm
# ==========================================


class _Layer:
    def __init__(self):
        # ['2020','2019']
        self.data_layer1 = list()
        # {'2020':['课标I','课标II']}
        self.data_layer2 = dict()
        # {'2020':[{'课标I':['语文','数学']},{'课标II':['语文','文数']}]}
        self.data_layer3 = dict()
        # {'2020':[{'课标I':[{'语文':['','']},{'数学':['','']}]},{'课标II':[{'语文':['','']},{'文数':['','']}]}]}
        self.data_layer4 = dict()
        # self._data_layer4 + download
        self.data_all = dict()
        # web 元素转化成文本数据
        self.data = dict()
        pass

    def set_labels(self, key1=None, key2=None, key3=None, labels=None):
        if labels is None:
            raise Exception('labels can not be None !')
        pass

    def get_labels(self, key1=None, key2=None, key3=None):
        if key1 == key2 == key3 is None:
            return self.data_layer1
        pass

    def get_data(self):
        return self.data

    def __str__(self):
        return self.data.__str__()


class Layer1(_Layer):
    """
    sample:
    ['2020','2019']

    key1 = key2 = key3 = None
    labels = ['2020','2019']
    """

    def set_labels(self, key1=None, key2=None, key3=None, labels=None):
        self.data_layer1 = labels
        _data = list()
        for label in labels:
            _data.append(label.text)
        self.data['ROOT'] = _data
        print('set_labels --> '+_data.__str__())
        pass


class Layer2(_Layer):
    """
    sample:
    {'2020':['课标I','课标II'],'2019':...}

    key1 = '2020'
    key2 = key3 = None
    labels = ['课标I','课标II']
    """

    def set_labels(self, key1=None, key2=None, key3=None, labels=None):
        if key1 is None:
            raise Exception('key1 can not be None !')
        self.data_layer2[key1] = labels
        _data = list()
        for label in labels:
            _data.append(label.text)
        self.data[key1] = _data
        print('set_labels --> ' + _data.__str__())
        pass

    def get_labels(self, key1=None, key2=None, key3=None):
        if key1 is None:
            raise Exception('key1 can not be None !')
        return self.data_layer2[key1]
        pass


class Layer3(_Layer):
    """
    sample:
    {'2020':[{'课标I':['语文','数学']},{'课标II':['语文','文数']}],'2019':...}

    key1 = '2020'
    key2 = '课标I'
    key3 = None
    labels = ['语文','数学']
    """

    def set_labels(self, key1=None, key2=None, key3=None, labels=None):
        if key1 is None:
            raise Exception('key1 can not be None !')
        elif key2 is None:
            raise Exception('key2 can not be None !')
        _layer2 = list()
        # layer2-layer3关联
        _label_dict = {str(key2): labels}
        # 提取label文本元素
        _data = list()
        for label in labels:
            _data.append(label.text)
        _data2 = {str(key2): _data}
        _data_layer2 = list()
        # 是否包含 key1
        if key1 in self.data_layer3:
            # 已经包含 key1 数据更新加入，获取已有列表 append
            _layer2 = self.data_layer3[key1]
            _layer2.append(_label_dict)
            _data_layer2 = self.data[key1]
            _data_layer2.append(_data2)
        else:
            # 不包含 key1 说明首次添加，layer2数据肯定也是初始状态，直接添加数据
            _layer2.append(_label_dict)
            self.data_layer3[key1] = _layer2
            _data_layer2.append(_data2)
            self.data[key1] = _data_layer2
        print('set_labels --> ' + _data.__str__())
        pass

    def get_labels(self, key1=None, key2=None, key3=None):
        if key1 is None:
            raise Exception('key1 can not be None !')
        if key2 is None:
            raise Exception('key2 can not be None !')
        if key1 in self.data_layer3:
            for dic in self.data_layer3[key1]:
                if key2 in dic:
                    return dic[key2]
        pass


class Layer4(_Layer):
    """
    sample:
    {'2020':[{'课标I':[{'语文':['','']},{'数学':['','']}]},{'课标II':[{'语文':['','']},{'文数':['','']}]}],'2019':...}

    key1 = '2020'
    key2 = '课标I'
    key3 = '语文'
    labels = ['论述类文本阅读','实用类文本阅读']
    """

    def __init__(self):
        super(Layer4, self).__init__()
        self._download = None

    def set_labels(self, key1=None, key2=None, key3=None, labels=None):
        if key1 is None:
            raise Exception('key1 can not be None !')
        elif key2 is None:
            raise Exception('key2 can not be None !')
        elif key3 is None:
            raise Exception('key3 can not be None !')
        # 提取label文本元素
        _data = list()
        for label in labels:
            _data.append(label.text)
        _layer2_data = list()
        _layer3_data = list()
        # 三四层关联
        _label_dict = {str(key3): labels}
        _layer2_label = list()
        _layer3_label = list()
        # 判断 key1 是否存在
        if key1 in self.data_layer4:
            # 取出已有第二层数据
            _layer2_label = self.data_layer4[key1]
            _layer2_data = self.data[key1]
            for layer2_d in _layer2_data:
                if key2 in layer2_d:
                    _layer3_data = layer2_d[key2]
                    _layer3_data.append(_data)
                pass
            for layer2 in _layer2_label:
                # 取出对应单个第二层数据
                if key2 in layer2:
                    # 获取第三层数据
                    _layer3_label = layer2[key2]
                    # 根据 key3 写入第四层数据
                    _layer3_label.append(_label_dict)
            pass
        else:
            # 不存在，首次添加
            _layer3_label.append(_label_dict)
            _layer2_label.append({str(key2): _layer3_label})
            self.data_layer4[key1] = _layer2_label
            _layer3_data.append(_data)
            _layer2_data.append({str(key2): _layer3_data})
            self.data[key1] = _layer2_data
        print('set_labels --> ' + _data.__str__())
        pass

    def get_labels(self, key1=None, key2=None, key3=None):
        if key1 is None:
            raise Exception('key1 can not be None !')
        elif key2 is None:
            raise Exception('key2 can not be None !')
        elif key3 is None:
            raise Exception('key3 can not be None !')
        if key1 in self.data_layer3:
            for dic in self.data_layer3[key1]:
                if key2 in dic:
                    for l3 in dic[key2]:
                        if key3 in l3:
                            return l3[key3]
        pass

    def set_download(self, down):
        self._download = down
        pass

    def get_download(self):
        return self._download

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

    def __str__(self):
        return self.layer1.__str__() + "\n" + self.layer2.__str__() + "\n" + self.layer3.__str__() + "\n" + self.layer4.__str__()
