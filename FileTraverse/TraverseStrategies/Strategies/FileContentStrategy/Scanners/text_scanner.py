from Expections.parameter_not_match_exception import ParameterNotMatchException
from FileTraverse.TraverseStrategies.Strategies.FileContentStrategy.abstract_file_scanner import AbstractFileScanner
from FileTraverse.TraverseStrategies.Strategies.FileContentStrategy.utils.scanner_text_utils import content_match
from Utils.file_mime_type_enums import FileMimeTypeEnums


class TextScanner(AbstractFileScanner):
    def support_scan(self, file_info):
        # 支持文本格式的扫描
        return file_info.get("mime_type_enum") == FileMimeTypeEnums.text

    def scan(self, file_info):
        if self.match_text is None:
            raise ParameterNotMatchException("未指定扫描文本")
        file_path = file_info.get("file_path")
        try:
            with open(file_path, "r", encoding=file_info.get("char_set")) as file:
                if not self.fuzzy_match:
                    content = file.read()
                    return content_match(content, self.match_text, False)
                else:
                    for line in file:
                        if content_match(line, self.match_text, True):
                            return True
                    return False
        except PermissionError:
            print("检查文件权限，当前文件已跳过")
            return False
        except UnicodeError:
            print(f"文件编码格式不支持,文件{file_path}")
            return False
        except IOError:
            print("IOError")
            return False

    def get_name(self):
        return "textScanner"
