import pdfplumber
from FileTraverse.TraverseStrategies.Strategies.FileContentStrategy.abstract_file_scanner import AbstractFileScanner
from Utils.file_mime_type_enums import FileMimeTypeEnums


class PdfScanner(AbstractFileScanner):
    def __init__(self):
        super().__init__()

    def scan(self, file_info):
        file_path = file_info["file_path"]
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if self.content_match(page_text):
                    return True
        return False

    def get_name(self):
        return "pdfScanner"

    def support_scan(self, file_info):
        mime_type_enum = file_info["mime_type_enum"]
        match mime_type_enum:
            case FileMimeTypeEnums.pdf:
                return True
        return False
