import xmind

class HtmOutput:
    def __init__(self):
        self.datas = []
        self.tree = None
        self.topic1 = list()
        self.topic2 = list()
        self.topic3 = list()

    def save_to_xmind(self, tree):
        self.tree = tree
        self.create_file()

    def create_file(self):
        x_file = xmind.load('53.xmind',)
        sheet1 = x_file.getPrimarySheet()
        # 设计画布样式
        sheet1.setTitle('五年高考三年模拟')
        root_topic = sheet1.getRootTopic()
        root_topic.setTitle('五年高考三年模拟 B版')
        # 创建第一层子话题
        for topic1 in self.tree.layer1.get_labels():
            s_topic = root_topic.addSubTopic()
            s_topic.setTitle(topic1.text)
            self.topic1.append(s_topic)
            for topic2 in self.tree.layer2.get_labels(topic1.text):
                s_topic2 = s_topic.addSubTopic()
                s_topic2.setTitle(topic2)
                self.topic2.append(s_topic2)
                for topic3 in self.tree.layer3.get_by_p_key(topic1.text):
                    for topic3_s in topic3.get(topic2):
                        s_topic3 = s_topic2.addSubTopic()
                        s_topic3.setTitle(topic3_s)
                        self.topic3.append(s_topic3)
        xmind.save(x_file, path='53.xmind')

