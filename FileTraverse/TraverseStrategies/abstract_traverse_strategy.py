from abc import abstractmethod


class AbstractTraverserStrategy:
    def __init__(self, order=1000):
        # 策略优先级，多个策略的时候生效
        self.order = order

    @abstractmethod
    def can_traverse(self, file_path):
        """
        :param file_path: 传入文件格式
        :return: 布尔类型
        """
        pass
