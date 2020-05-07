class HtmParser:

    def __init__(self):
        self.labels = None

    def set_labels(self, labels):
        self.labels = labels

    def parse_layer1(self):
        # 获取第一层
        layer1 = []
        try:
            for label in self.labels:
                data_layer = label.get_attribute('data-layer')
                if data_layer == '1':
                    layer1.append(label)
        except Exception as e:
            print(e)
        return layer1

    def parse_layer2(self):
        # 获取第二层
        layer2 = []
        for label in self.labels:
            try:
                data_layer = label.get_attribute('data-layer')
                if data_layer == '2':
                    layer2.append(label)
            except Exception as e:
                print(e)
        return layer2

    def parse_layer3(self):
        # 获取第三层
        layer3 = []
        try:
            for label in self.labels:
                data_layer = label.get_attribute('data-layer')
                if data_layer == '3':
                    layer3.append(label)
        except Exception as e:
            print(e)
        return layer3
