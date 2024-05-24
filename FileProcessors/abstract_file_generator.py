from abc import abstractmethod


class AbstractFileGenerator:
    def __init__(self):
        self.generate_path = None

    def set_generate_path(self, path):
        self.generate_path = path

    @abstractmethod
    def support_generate(self, file_path):
        pass

    @abstractmethod
    def generate(self, file_name, content):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def post_process(self):
        """
        后置处理方法，当处理器处理完成后，会在
        :return:
        """
        pass
