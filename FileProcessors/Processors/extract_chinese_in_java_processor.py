import os.path
import re

from FileProcessors.abstract_file_processor import AbstractFileProcessor


class ExtractChineseInJavaProcessor(AbstractFileProcessor):

    def __init__(self):
        super().__init__()
        self.generators = list()

    def get_name(self):
        return "extractChineseInJavaProcessor"

    def support_process(self, file_path):
        return file_path.endswith('.java')

    def process(self, file_path):
        java_package = None
        file_chinese_list = list()
        with open(file_path, "r", encoding="utf-8") as f:
            multi_annotation = False
            row_num = 0
            for line in f:
                row_num += 1
                line = line.strip()
                if line.startswith("package"):
                    java_package = line.strip("package").strip(";")
                    file_name = os.path.basename(file_path)
                    java_package = java_package + "(" + file_name + ")"
                # 单行注释的处理
                if line.startswith("//"):
                    continue

                # 多行注释的处理
                if line.startswith("/*"):
                    multi_annotation = True
                if line.startswith("*/"):
                    multi_annotation = False
                    continue
                if multi_annotation:
                    continue
                # 行内的处理
                current_chinese = self._process_single_line(line)
                if len(current_chinese) > 0 and self._contains_chinese(current_chinese):
                    # 判断本行是否不包含中文，不包含中文的就去掉
                    chinese_include_row = list()
                    row_number = "行号:" + str(row_num)
                    chinese_include_row.append(row_number)
                    chinese_include_row.append(line)
                    file_chinese_list.append(chinese_include_row)
        if len(file_chinese_list) > 0:
            for generator in self.generators:
                generator.generate(java_package, file_chinese_list)

    def post_process(self):
        for generator in self.generators:
            generator.post_process()

    @staticmethod
    def _process_single_line(line):
        into_chinese = False
        current_chinese = ""
        strip_annotation_index = line.find("//")
        if strip_annotation_index != -1:
            line = line[:strip_annotation_index]
        for content in line:
            if content == "\"":
                if into_chinese:
                    into_chinese = False
                else:
                    into_chinese = True
                    continue
            if into_chinese:
                current_chinese += content
        return current_chinese

    @staticmethod
    def _contains_chinese(text):
        pattern = re.compile(r'[\u4e00-\u9fff]')  # 匹配中文字符的正则表达式范围
        return bool(pattern.search(text))
