from fuzzywuzzy import fuzz

from Expections.parameter_not_match_exception import ParameterNotMatchException
from FileTraverse.TraverseStrategies.Strategies.FileContentStrategy.abstract_file_scanner import AbstractFileScanner
from Utils.file_mime_type_enums import FileMimeTypeEnums


class TextScanner(AbstractFileScanner):
    def support_scan(self, file_info):
        # 支持文本格式的扫描
        return file_info.get("mime_type_enum") == FileMimeTypeEnums.text

    def scan(self, file_info):
        if self.match_text is None:
            raise ParameterNotMatchException("未指定扫描文本")
        try:
            file_path = file_info.get("file_path")
            with open(file_path, "r", encoding=file_info.get("char_set")) as file:
                if not self.fuzzy_match:
                    content = file.read()
                    if self.match_text in content:
                        return True
                    else:
                        return False
                else:
                    for line in file:
                        if fuzz.partial_ratio(line.strip("\n"), self.match_text) >= 80:
                            return True
                    return False
        except PermissionError:
            print("检查文件权限，当前文件已跳过")
            return False
        except UnicodeError:
            print("文件编码格式不支持")
            return False
        except IOError:
            print("IOError")
            return False
