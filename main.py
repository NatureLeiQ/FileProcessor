import time

from Dispatcher.dispatcher import Dispatcher
from FileProcessors.Generators.all_to_one_excel_generator import AllToOneExcelGenerator
from FileProcessors.Generators.one_to_one_text_generator import OneToOneTextGenerator
from FileTraverse.TraverseStrategies.Strategies.dir_name_strategy import DirNameStrategy
from FileTraverse.TraverseStrategies.Strategies.suffix_traverse_strategy import SuffixTraverseStrategy
from FileTraverse.TraverseStrategies.Strategies.FileContentStrategy.file_content_strategy import FileContentStrategy
from FileTraverse.TraverseStrategies.traverse_strategy_action_model_enum import TraverseStrategyActionModelEnum
from FileProcessors.Processors.log_file_path_processor import LogFilePathProcessor

if __name__ == '__main__':
    root_directory = r"your\file\path"  # 根目录
    generate_path = r"file\generation\path"
    strategies = list()
    strategies.append(FileContentStrategy("匹配的内容", ["具体的扫描器"], False))

    specify_processors = ["logFilePathProcessor"]
    generators = list()
    generators.append(AllToOneExcelGenerator())
    dispatcher = Dispatcher(root_directory, generate_path, strategies,
                            TraverseStrategyActionModelEnum.FULL_SATISFACTION,
                            generators,
                            None, specify_processors)
    begin_time = time.time()
    dispatcher.run()
    end_time = time.time()
    time_consume = end_time - begin_time
    print(f"耗时：{time_consume}秒")


