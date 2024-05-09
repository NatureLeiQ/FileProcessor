from abc import abstractmethod


class AbstractFileScanner:

    @abstractmethod
    def scan(self, file_path):
        pass
