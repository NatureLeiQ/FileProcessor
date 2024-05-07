from abc import abstractmethod


class AbstractFileGenerator:

    @abstractmethod
    def set_generate_path(self, path):
        pass

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
