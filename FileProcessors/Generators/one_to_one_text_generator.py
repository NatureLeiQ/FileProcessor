import os
import random

from FileProcessors.abstract_file_generator import AbstractFileGenerator


class OneToOneTextGenerator(AbstractFileGenerator):

    def get_name(self):
        return "oneToOneTextGenerator"

    def __init__(self):
        super().__init__()
        self.generate_path = None

    def support_generate(self, file_path):
        return True

    def post_process(self):
        pass

    def generate(self, file_name, content):
        generate_file_path = os.path.join(self.generate_path, file_name + ".txt")
        if os.path.isfile(generate_file_path):
            generate_file_path = os.path.join(self.generate_path, file_name + str(random.randint(0, 100)) + ".txt")
        with open(generate_file_path, "w", encoding="utf-8") as f:
            try:
                lines = content.split("\n")
            except Exception:
                print(content)
            for line in lines:
                if isinstance(line, list):
                    line = "    ".join(line)
                f.write(line + "\n")
