from abc import abstractmethod


class AbstractFileScanner:
    def __init__(self):
        self.match_text = None
        self.fuzzy_match = True

    def set_match_text(self, match_text):
        self.match_text = match_text

    def set_fuzzy_match(self, fuzzy_match):
        self.fuzzy_match = fuzzy_match

    @abstractmethod
    def scan(self, file_info):
        """
        返回文件中是否能匹配到
        """
        pass

    @abstractmethod
    def support_scan(self, file_info):
        pass

    @abstractmethod
    def get_name(self):
        pass
