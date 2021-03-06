import xmind


class HtmOutput:
    def __init__(self):
        self.tree = None
        self.topic1 = list()
        self.topic2 = list()
        self.topic3 = list()
        self.topic4 = list()

    def save_to_xmind(self, tree):
        self.tree = tree
        self.create_file()

    def create_file(self):
        x_file = xmind.load('53.xmind', )
        sheet1 = x_file.getPrimarySheet()
        # 设计画布样式
        sheet1.setTitle('五年高考三年模拟')
        root_topic = sheet1.getRootTopic()
        root_topic.setTitle('五年高考三年模拟 B版')
        # 创建第一层子话题
        for topic1 in self.tree.layer1.get_data()['ROOT']:
            s_topic = root_topic.addSubTopic()
            s_topic.setTitle(topic1)
            self.topic1.append(s_topic)
            for topic2 in self.tree.layer2.get_data()[topic1]:
                s_topic2 = s_topic.addSubTopic()
                s_topic2.setTitle(topic2)
                self.topic2.append(s_topic2)
                for layer2 in self.tree.layer3.get_data()[topic1]:
                    for item_layer2 in layer2:
                        if topic2 in item_layer2:
                            for topic3 in layer2[item_layer2]:
                                s_topic3 = s_topic2.addSubTopic()
                                s_topic3.setTitle(topic3)
                                self.topic3.append(s_topic3)
                                # 最后一层
                                for l4_layer2 in self.tree.layer4.get_data()[topic1]:
                                    for l4_item_layer2 in l4_layer2:
                                        if topic2 in l4_item_layer2:
                                            for l4_topic3 in l4_layer2[l4_item_layer2]:
                                                if topic3 in l4_topic3:
                                                    for _key in l4_topic3[topic3]:
                                                        s_topic4 = s_topic3.addSubTopic()
                                                        s_topic4.setTitle(_key)
                                                        self.topic4.append(s_topic4)
        xmind.save(x_file, path='53.xmind')
