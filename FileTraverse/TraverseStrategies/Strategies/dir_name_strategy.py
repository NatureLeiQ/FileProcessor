import os

from FileTraverse.TraverseStrategies.abstract_traverse_strategy import AbstractTraverserStrategy


class DirNameStrategy(AbstractTraverserStrategy):
    """
    文件夹名称策略
    """
    def __init__(self, dir_names, include=True):
        self.dir_names = dir_names
        self.include = include  # include=True表示只检查这个包下面的，include=False表示排除这个包下面的

    def can_traverse(self, file_path):
        normpath = os.path.normpath(file_path)
        split_path = normpath.split(os.sep)
        if isinstance(self.dir_names, list):
            for dir_name in self.dir_names:
                # 当传入多个文件夹， 且include=True，当分割的路径中有一个满足文件夹名称就可以遍历。当include=False,分割的路径中有一个满足文件夹名称，就不能遍历
                contain = self._contains_dir(split_path, dir_name)
                if not self.include and contain:
                    return False
                if self.include and contain:
                    return True
            # 执行到这里， 说明不包括的文件夹一个都没有找到，那么就可以执行
            if not self.include:
                return True
            else:
                return False
        else:
            if self.include:
                return self._contains_dir(split_path, self.dir_names)
            else:
                return not self._contains_dir(split_path, self.dir_names)

    @staticmethod
    def _contains_dir(split_path, dir_name):
        return dir_name in split_path



