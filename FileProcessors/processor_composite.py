from Expections.processors_not_config_exception import ProcessorsNotConfigException


class ProcessorComposite:
    def __init__(self, processors):
        self.processors = processors

    def process(self, file_path):
        if self.processors is None:
            raise ProcessorsNotConfigException("未配置文件处理器")
        for processor in self.processors:
            if processor.support_process(file_path) and processor.support_generate(file_path):
                processor.process(file_path)
                break

