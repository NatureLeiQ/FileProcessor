from abc import abstractmethod


class AbstractFileProcessor:
    def __init__(self):
        self.generate_path = None
        self.generators = list()

    @abstractmethod
    def support_process(self, file_path):
        pass

    def set_generator(self, generator):
        if isinstance(generator, list):
            self.generators.extend(generator)
        else:
            self.generators.append(generator)

    def support_generate(self, path):
        for generator in self.generators:
            # 默认有一个生成器可以生成，就返回true
            if generator.support_generate(path):
                return True
        return False

    @abstractmethod
    def process(self, file_path):
        pass

    @abstractmethod
    def post_process(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
