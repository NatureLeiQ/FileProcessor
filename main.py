from Dispatcher.dispatcher import Dispatcher
from FileProcessors.Generators.one_to_one_text_generator import OneToOneTextGenerator
from FileProcessors.Generators.all_to_one_excel_generator import AllToOneExcelGenerator
from FileTraverse.TraverseStrategies.Strategies.dir_name_strategy import DirNameStrategy
from FileTraverse.TraverseStrategies.Strategies.suffix_traverse_strategy import SuffixTraverseStrategy
from FileTraverse.TraverseStrategies.traverse_strategy_action_model_enum import TraverseStrategyActionModelEnum

if __name__ == '__main__':
    root_directory = r"your\file\path"  # 根目录
    generate_path = r"file\generation\path"  # 生成的目录
    strategies = list()
    strategies.append(SuffixTraverseStrategy(".properties"))
    strategies.append(DirNameStrategy("i18n"))
    strategies.append(DirNameStrategy("target", False))
    specify_processors = ["propertiesChineseProcessor"]
    generators = list()
    generators.append(OneToOneTextGenerator())
    generators.append(AllToOneExcelGenerator())
    dispatcher = Dispatcher(root_directory, generate_path, strategies,
                            TraverseStrategyActionModelEnum.FULL_SATISFACTION,
                            generators,
                            None, specify_processors)
    dispatcher.run()
