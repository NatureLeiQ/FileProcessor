from FileProcessors.abstract_file_processor import AbstractFileProcessor
from Utils.file_mime_type_enums import FileMimeTypeEnums
from Utils.file_unit_enums import FileUnitEnums
from Utils.file_utils import get_file_unit_size, decide_file_type_by_encode, resolve_file_path


class TextParseProcessor(AbstractFileProcessor):
    """
        文本解析处理器：用于解析未知格式的文本文档，生成txt格式，并且文件名包含正确的编码格式，文本大小需要小于100m。
    """

    def __init__(self):
        super().__init__()

    def support_process(self, file_path):
        file_type_info = decide_file_type_by_encode(file_path)
        if file_type_info["mime_type_enum"] == FileMimeTypeEnums.unknown:
            return False
        file_mb_size = get_file_unit_size(file_path, FileUnitEnums.MB)
        return file_mb_size <= 100

    def process(self, file_path):
        file_type_info = decide_file_type_by_encode(file_path)
        char_set = file_type_info["char_set"]
        with open(file_path, "r", encoding=char_set) as f:
            content = f.read()
        # 调用生成器生成对应的文件
        if content is None:
            return
        resolved_file_path = resolve_file_path(file_path)
        file_name = resolved_file_path["file_name"]
        if file_name is None:
            file_name = "defaultTextParseFile"
        for generator in self.generators:
            generator.generate(file_name, content)

    def post_process(self):
        pass

    def get_name(self):
        return "textParseProcessor"
