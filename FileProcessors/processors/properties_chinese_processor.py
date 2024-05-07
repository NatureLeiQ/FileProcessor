import os
import re

from FileProcessors.abstract_file_processor import AbstractFileProcessor
from Utils.encode_decode_utils import get_unicode_decode


class PropertiesChineseProcessor(AbstractFileProcessor):

    def __init__(self):
        self.generate_path = None
        self.generators = list()

    def set_generator(self, generator):
        if isinstance(generator, list):
            self.generators.extend(generator)
        else:
            self.generators.append(generator)

    def support_generate(self, path):
        for generator in self.generators:
            # 默认有一个生成器可以生成，就返回true
            if generator.support_generate(path):
                return True
        return False

    def support_process(self, file_path):
        return file_path.endswith('.properties')

    def get_name(self):
        return "propertiesChineseProcessor"

    def post_process(self):
        for generator in self.generators:
            generator.post_process()

    def process_internal(self, file_path):
        file_chinese_list = list()
        with open(file_path, "r", encoding="utf-8") as f:
            row_num = 0
            for line in f:
                row_num += 1
                line = line.strip()
                strip_annotation_index = line.find("=")
                if strip_annotation_index == -1:
                    continue
                else:
                    en_line = line[:strip_annotation_index]  # 英文内容
                    line = line[strip_annotation_index + 1:]
                    if len(line) > 0:
                        line = get_unicode_decode(line)
                if len(line) > 0 and self._contains_chinese(line):
                    # 判断本行是否不包含中文，不包含中文的就去掉
                    chinese_include_row = list()
                    row_number = "行号:" + str(row_num)
                    chinese_include_row.append(row_number)
                    chinese_include_row.append(en_line)
                    chinese_include_row.append(line)
                    file_chinese_list.append(chinese_include_row)

            if len(file_chinese_list) > 0:
                dir_name, _ = os.path.splitext(file_path)
                file_base_name = os.path.basename(file_path).split(".")
                file_name = dir_name + file_base_name[0]
                file_name = file_name.replace('/', '').replace('\\', '')
                for generator in self.generators:
                    generator.generate(file_name, file_chinese_list)

    @staticmethod
    def _contains_chinese(text):
        pattern = re.compile(r'[\u4e00-\u9fff]')  # 匹配中文字符的正则表达式范围
        return bool(pattern.search(text))
