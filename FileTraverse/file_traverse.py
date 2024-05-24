import os

from alive_progress import alive_bar

from Expections.parameter_not_match_exception import ParameterNotMatchException


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
        if os.path.isfile(self.root_path):
            self._traverse_file()
        elif os.path.isdir(self.root_path):
            self._traverse_dir()
        else:
            raise ParameterNotMatchException(f"传入的处理路径不规范：{self.root_path}")

    def _expect_traverse(self, file_path):
        """
        预期是否可被遍历，由遍历策略决定
        :return: 布尔值
        """
        self.strategy_manager.set_current_file(file_path)
        return self.strategy_manager.should_process()

    def _count_traverse_dir_nums(self):
        count = 0
        for _, _, _ in os.walk(self.root_path):
            count += 1
        return count

    def _traverse_file(self):
        if self._expect_traverse(self.root_path):
            self.traverse_paths.append(self.root_path)

    def _traverse_dir(self):
        traverse_dir_nums = self._count_traverse_dir_nums()
        with alive_bar(total=traverse_dir_nums, title="文件夹遍历中:", bar='smooth', force_tty=True) as dir_bar:
            for root, dirs, files in os.walk(self.root_path):
                dir_bar()
                dir_bar.text = f"当前文件夹：{root}"
                for name in files:
                    file_path = os.path.join(root, name)
                    if self._expect_traverse(file_path):
                        self.traverse_paths.append(file_path)
