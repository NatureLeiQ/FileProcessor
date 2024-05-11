import os

from Expections.generator_name_not_exist_exception import GeneratorNameNotExistException
from Expections.generators_not_config_exception import GeneratorsNotConfigException
from Expections.method_not_support_exception import MethodNotSupportException
from Expections.processors_not_config_exception import ProcessorsNotConfigException
from FileProcessors.abstract_file_processor import AbstractFileProcessor
from Utils.import_utils import load_modules_from_folder


class ProcessorComposite(AbstractFileProcessor):
    def __init__(self, specify_processors, generators, generate_path):

        self.generators = generators
        self._check_generators()
        self.specify_processors = specify_processors
        self.generate_path = generate_path
        self.processors = self._config_processors()

    def _check_generators(self):
        if len(self.generators) <= 0:
            raise GeneratorsNotConfigException("未配置文件生成器")

    def _config_processors(self):
        """
            配置文件处理器
        """
        config_result_processors = list()
        file_processors = load_modules_from_folder("FileProcessors/Processors")
        specify_processor = False
        if self.specify_processors is not None:
            specify_processor = True
        for processor in file_processors:
            processor_name = processor.get_name()
            if processor_name is None:
                continue
            if specify_processor:
                if processor_name in self.specify_processors:
                    config_result_processors.append(processor)
            else:
                config_result_processors.append(processor)
        for processor in config_result_processors:
            for generator in self.generators:
                if generator.get_name() is None or generator.get_name().strip() == "":
                    raise GeneratorNameNotExistException("当前生成器的名称未配置" + str(generator))
                generate_path_with_name = os.path.join(self.generate_path, generator.get_name())
                if not os.path.exists(generate_path_with_name):
                    os.makedirs(generate_path_with_name)
                generator.set_generate_path(generate_path_with_name)
            processor.set_generator(self.generators)

        return config_result_processors

    def process(self, file_path):
        if self.processors is None:
            raise ProcessorsNotConfigException("未配置文件处理器")
        for processor in self.processors:
            if processor.support_process(file_path) and processor.support_generate(file_path):
                processor.process(file_path)
                processor.post_process()
                break

    def support_process(self, file_path):
        raise MethodNotSupportException("处理器方法由内部管理，不对外部实现")

    def set_generator(self, generator):
        raise MethodNotSupportException("处理器方法由内部管理，不对外部实现")

    def support_generate(self, path):
        raise MethodNotSupportException("处理器方法由内部管理，不对外部实现")

    def post_process(self):
        raise MethodNotSupportException("处理器方法由内部管理，不对外部实现")

    def get_name(self):
        return "processorComposite"
