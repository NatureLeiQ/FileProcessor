import time

from Dispatcher.dispatcher import Dispatcher
from FileProcessors.Generators.one_to_one_text_generator import OneToOneTextGenerator
from FileTraverse.TraverseStrategies.traverse_strategy_action_model_enum import TraverseStrategyActionModelEnum

if __name__ == '__main__':
    root_directory = r"your\file\path"  # 根目录
    generate_path = r"file\generation\path"

    specify_processors = ["textParseProcessor"]
    generators = list()
    generators.append(OneToOneTextGenerator())
    dispatcher = Dispatcher(root_directory, generate_path, None,
                            TraverseStrategyActionModelEnum.FULL_SATISFACTION,
                            generators,
                            None, specify_processors)
    begin_time = time.time()
    dispatcher.run()
    end_time = time.time()
    time_consume = end_time - begin_time
    print(f"耗时：{time_consume}秒")
