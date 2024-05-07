import os


class FileTraverse:
    def __init__(self, root_path, strategy_manager):
        """
        文件遍历器
        :param root_path: 遍历根目录
        :param strategy_manager 策略管理器
        """
        self.root_path = root_path
        self.strategy_manager = strategy_manager
        self.traverse_paths = list()

    def traverse(self):
        for root, dirs, files in os.walk(self.root_path):
            for name in files:
                file_path = os.path.join(root, name)
                if self._expect_traverse(file_path):
                    self.traverse_paths.append(file_path)

    def _expect_traverse(self, file_path):
        """
        预期是否可被遍历，由遍历策略决定
        :return: 布尔值
        """
        self.strategy_manager.set_current_file(file_path)
        return self.strategy_manager.should_process()
