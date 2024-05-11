import warnings

from Expections.method_not_support_exception import MethodNotSupportException
from Expections.parameter_not_match_exception import ParameterNotMatchException
from Expections.scanners_not_config_exception import ScannersNotConfigException
from FileTraverse.TraverseStrategies.Strategies.FileContentStrategy.abstract_file_scanner import AbstractFileScanner
from Utils.import_utils import load_modules_from_folder


class ScannerComposite(AbstractFileScanner):

    def __init__(self, match_text, specify_scanners, fuzzy_match):
        super().__init__()
        self.match_text = match_text
        self.fuzzy_match = fuzzy_match
        if specify_scanners is not None:
            if not isinstance(specify_scanners, list):
                specify_scanners = [specify_scanners]
        self.specify_scanners = specify_scanners
        self.scanners = self._config_scanners()

    def _config_scanners(self):
        scanners = load_modules_from_folder("FileTraverse/TraverseStrategies/Strategies/FileContentStrategy/Scanners")
        if len(scanners) <= 0:
            raise ScannersNotConfigException("未找到可用的扫描器")
        config_result_scanners = list()
        if self.specify_scanners is not None:
            for scanner in scanners:
                if scanner.get_name() in self.specify_scanners:
                    config_result_scanners.append(scanner)
        else:
            config_result_scanners = scanners

        if len(config_result_scanners) <= 0:
            raise ParameterNotMatchException("指定的扫描器不存在")

        if self.specify_scanners is not None and len(config_result_scanners) < len(self.specify_scanners):
            valid_scanner_names = [scanner.get_name() for scanner in config_result_scanners]
            warnings.warn(f"指定的扫描器未全部生效，已生效扫描器如下{valid_scanner_names}")
        for scanner in config_result_scanners:
            scanner.set_match_text(self.match_text)
            scanner.set_fuzzy_match(self.fuzzy_match)
        return config_result_scanners

    def scan(self, file_info):
        for scanner in self.scanners:
            if scanner.support_scan(file_info):
                return scanner.scan(file_info)

    def support_scan(self, file_info):
        raise MethodNotSupportException("扫描器方法由内部管理，不对外部实现")

    def get_name(self):
        return "scannerComposite"
