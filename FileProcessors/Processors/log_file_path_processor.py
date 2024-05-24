from FileProcessors.abstract_file_processor import AbstractFileProcessor


class LogFilePathProcessor(AbstractFileProcessor):
    def __init__(self):
        super().__init__()
        self.paths = list()
        self.generators = None

    def support_process(self, file_path):
        return True

    def process(self, file_path):
        for generator in self.generators:
            generator.generate(file_path, None)

    def post_process(self):
        for generator in self.generators:
            generator.post_process()

    def get_name(self):
        return "logFilePathProcessor"
