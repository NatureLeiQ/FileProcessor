import os.path

from openpyxl import Workbook

from FileProcessors.abstract_file_generator import AbstractFileGenerator


class AllToOneExcelGenerator(AbstractFileGenerator):

    def __init__(self, file_name=None):
        super().__init__()
        self.all_contents = list()  # 保存二维列表
        self.file_name = file_name

    def support_generate(self, file_path):
        return True

    def get_name(self):
        return "allToOneExcelGenerator"

    def post_process(self):
        # 将所有的元素集中到一个excel文件里面
        if self.file_name is None:
            self.file_name = "allToOneExcelGeneratorGenerated"
        if self.all_contents == "" or self.all_contents is None:
            return
        wb = Workbook()
        ws = wb.active
        for contents in self.all_contents:
            if self._judge_two_dim(contents):
                for content in contents:
                    ws.append(content)
            else:
                ws.append(contents)
        save_path = str(os.path.join(self.generate_path, self.file_name + ".xlsx"))
        wb.save(save_path)

    def generate(self, file_name, content):
        if file_name is not None:
            if isinstance(file_name, str):
                file_name = [file_name]
            self.all_contents.append(file_name)
        if content is not None:
            if isinstance(content, str):
                content = [content]
            self.all_contents.append(content)

    @staticmethod
    def _judge_two_dim(contents):
        if not isinstance(contents, list):
            return False
        for content in contents:
            if not isinstance(content, list):
                return False
            return True
