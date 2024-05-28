import os
import random

from FileProcessors.abstract_file_generator import AbstractFileGenerator


class PropertiesGenerator(AbstractFileGenerator):

    def support_generate(self, file_path):
        return True

    def generate(self, file_name, content):
        generate_file_path = os.path.join(self.generate_path, file_name + ".properties")
        if os.path.isfile(generate_file_path):
            generate_file_path = os.path.join(self.generate_path, file_name + str(random.randint(0, 100)) + ".properties")
        with open(generate_file_path, "w", encoding="utf-8") as f:
            for line in content:
                f.write(line + "\n")

    def get_name(self):
        return "propertiesGenerator"

    def post_process(self):
        pass