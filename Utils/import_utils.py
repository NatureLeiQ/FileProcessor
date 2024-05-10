import importlib.util
import os


def load_modules_from_folder(folder_path, package_name=''):
    """
    加载指定文件夹下的所有 Python 文件（作为模块）。

    注意：这个函数只是执行了文件，但并未真正将它们作为模块导入到 sys.modules 中。
    如果你想要将它们作为包的一部分导入，你需要设置正确的 package_name。

    :param folder_path: 文件夹路径
    :param package_name: 可选的包名（如果文件夹是一个包的一部分）
    """
    modules = list()
    for filename in os.listdir(folder_path):
        if filename.endswith('.py') and not filename.startswith('_'):  # 忽略以 _ 开头的文件和 __init__.py
            module_name = os.path.splitext(filename)[0]
            module_spec = importlib.util.spec_from_file_location(
                '{}.{}'.format(package_name, module_name),
                os.path.join(folder_path, filename)
            )
            if module_spec is not None:
                module = importlib.util.module_from_spec(module_spec)
                module_spec.loader.exec_module(module)
                for name, obj in vars(module).items():
                    if isinstance(obj, type):
                        # 检查是否为类且不是内置类型或模块等
                        if hasattr(obj, '__module__') and (module.__name__ == obj.__module__):
                            # 创建一个类的实例
                            try:
                                instance = obj()
                                modules.append(instance)
                                # print(f"Created instance of {name} from {modname}")
                            except TypeError:
                                # 如果类没有无参数的构造函数，则会抛出TypeError
                                print(f"Cannot create instance of {name} without arguments")

                # 此时，module 变量引用了文件的内容，但并未作为模块导入到 sys.modules
    return modules
