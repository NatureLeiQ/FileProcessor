from abc import abstractmethod


class AbstractFileProcessor:

    @abstractmethod
    def support_process(self, file_path):
        pass

    @abstractmethod
    def set_generator(self, generator):
        # 可配置多个生成器，这样可以生成多个类型的文件
        pass

    @abstractmethod
    def support_generate(self, path):
        pass

    def process(self, file_path):
        self.process_internal(file_path)
        self.post_process()

    @abstractmethod
    def process_internal(self, file_path):
        pass

    @abstractmethod
    def post_process(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
