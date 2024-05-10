from abc import abstractmethod


class AbstractFileScanner:
    def __init__(self):
        self.match_text = None
        self.accurate = True

    def set_match_text(self, match_text):
        self.match_text = match_text

    def set_accurate(self, accurate):
        self.accurate = accurate

    @abstractmethod
    def scan(self, file_path):
        """
        返回文件中是否能匹配到
        """
        pass

    @abstractmethod
    def support_scan(self, file_info):
        pass
