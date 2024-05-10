from FileTraverse.TraverseStrategies.Strategies.FileContentStrategy.file_type_decider import FileTypeDecider
from FileTraverse.TraverseStrategies.Strategies.FileContentStrategy.scanner_composite import ScannerComposite
from FileTraverse.TraverseStrategies.abstract_traverse_strategy import AbstractTraverserStrategy


class FileContentStrategy(AbstractTraverserStrategy):
    """
    文件内容策略，对文件的内容进行检索，最终可生成 判定策略这样的流程：
    通过判定器，判定文件类型，然后找到对应的扫描器进行扫描，扫描后如果满足条件，就返回。注意一个文件中可能有多个满足条件的位置，扫描器返回应该针对不同的类型返回详细的位置信息（文本文件就是第几行，excel也是第几个sheet
    第几行，word是第几页，pdf也是第几页，）
    不同的扫描器处理不同的文件。尽量运用多线程技术来进行处理，因为文件可能很多.扫描器只是扫描不进行处理，依旧属于文件遍历的范畴
    """

    def __init__(self, match_text, accurate=True, order=10):
        super().__init__(order)  # 需要把当前策略的优先级降低
        self.file_type_decider = FileTypeDecider()
        self.scanner_composite = ScannerComposite(match_text, accurate)

    def can_traverse(self, file_path):
        file_type_info = self.file_type_decider.decide_file_type(file_path)
        file_type_info["file_path"] = file_path
        return self.scanner_composite.scan(file_type_info)
