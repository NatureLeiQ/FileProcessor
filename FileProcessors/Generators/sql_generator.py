import os
import random

from FileProcessors.abstract_file_generator import AbstractFileGenerator


class SQLGenerator(AbstractFileGenerator):
    def __init__(self):
        super().__init__()

    def support_generate(self, file_path):
        return True

    def generate(self, file_name, content):
        generate_file_path = os.path.join(self.generate_path, file_name + ".sql")
        if os.path.isfile(generate_file_path):
            generate_file_path = os.path.join(self.generate_path, file_name + str(random.randint(0, 100)) + ".sql")
        with open(generate_file_path, "w", encoding="utf-8") as f:
            lines = content.split("\n")
            for line in lines:
                f.write(line + "\n")

    def get_name(self):
        return "sqlGenerator"

    def post_process(self):
        pass
