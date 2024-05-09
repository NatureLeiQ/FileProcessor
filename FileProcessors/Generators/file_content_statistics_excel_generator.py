from FileProcessors.abstract_file_generator import AbstractFileGenerator


class FileContentStatisticsExcelGenerator(AbstractFileGenerator):
    """
    TODO
     统计文件夹下面的包含某种类型的文件内容，并整理到excel中
    """
    def set_generate_path(self, path):
        pass

    def support_generate(self, file_path):
        pass

    def get_name(self):
        return "fileContentStatisticsExcelGenerator"

    def generate(self, file_name, content):
        pass

    def post_process(self):
        pass
