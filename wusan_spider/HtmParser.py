class HtmParser:

    def __init__(self):
        self.labels = None

    def set_labels(self, labels):
        self.labels = labels

    def parse_layer1(self):
        # 获取第一层
        layer1 = []
        for label in self.labels:
            data_layer = label.get_attribute('data-layer')
            if data_layer == '1':
                layer1.append(label)
        return layer1

    def parse_layer2(self):
        # 获取第二层
        layer2 = []
        for label in self.labels:
            data_layer = label.get_attribute('data-layer')
            if data_layer == '2':
                layer2.append(label)
        return layer2

    def parse_layer3(self):
        # 获取第三层
        layer3 = []
        for label in self.labels:
            data_layer = label.get_attribute('data-layer')
            if data_layer == '3':
                layer3.append(label)
        return layer3

    def parse_layer4(self):
        # 获取第四层
        layer4 = []
        for span in self.labels:
            data_layer = span.get_attribute('class')
            if data_layer == 'title':
                layer4.append(span)
        return layer4
