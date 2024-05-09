from abc import abstractmethod


class AbstractTraverserStrategy:

    @abstractmethod
    def can_traverse(self, file_path):
        """
        :param file_path: 传入文件格式
        :return: 布尔类型
        """
        pass
