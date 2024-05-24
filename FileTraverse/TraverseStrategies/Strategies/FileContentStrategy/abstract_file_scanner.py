from abc import abstractmethod

from fuzzywuzzy import fuzz


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

    def content_match(self, content, match_text=None, fuzzy_match=None):
        if match_text is None:
            match_text = self.match_text
        if fuzzy_match is None:
            fuzzy_match = self.fuzzy_match

        if not fuzzy_match:
            if match_text in content:
                return True
            else:
                return False
        else:
            if fuzz.partial_ratio(content.strip("\n"), match_text) >= 80:
                return True
            return False
