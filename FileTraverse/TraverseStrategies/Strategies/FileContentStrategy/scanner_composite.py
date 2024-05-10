from Expections.method_not_support_exception import MethodNotSupportException
from Expections.scanners_not_config_exception import ScannersNotConfigException
from FileTraverse.TraverseStrategies.Strategies.FileContentStrategy.abstract_file_scanner import AbstractFileScanner
from Utils.import_utils import load_modules_from_folder


class ScannerComposite(AbstractFileScanner):

    def __init__(self, match_text, accurate):
        super().__init__()
        self.match_text = match_text
        self.accurate = accurate
        self.scanners = self._config_scanners()

    def _config_scanners(self):
        scanners = load_modules_from_folder("FileTraverse/TraverseStrategies/Strategies/FileContentStrategy/Scanners")
        if len(scanners) <= 0:
            raise ScannersNotConfigException("未找到可用的扫描器")
        for scanner in scanners:
            scanner.set_match_text(self.match_text)
            scanner.set_accurate(self.accurate)
        return scanners

    def scan(self, file_info):
        for scanner in self.scanners:
            if scanner.support_scan(file_info):
                scanner.set_content()
                return scanner.scan(file_info)

    def support_scan(self, file_info):
        raise MethodNotSupportException("扫描器方法由内部管理，不对外部实现")
