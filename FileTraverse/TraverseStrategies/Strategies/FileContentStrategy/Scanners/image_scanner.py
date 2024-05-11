# from PIL import Image
# from easyocr import easyocr
# from fuzzywuzzy import fuzz
#
# from Expections.parameter_not_match_exception import ParameterNotMatchException
# from FileTraverse.TraverseStrategies.Strategies.FileContentStrategy.abstract_file_scanner import AbstractFileScanner
# from Utils.file_mime_type_enums import FileMimeTypeEnums
# from Utils.class_utils import deprecated
#
#
# class ImageScanner(AbstractFileScanner):
#
#     @deprecated
#     def __init__(self):
#         super().__init__()
#         self.image_reader = easyocr.Reader(['ch_sim', 'en'])
#
#     def get_name(self):
#         return "imageScanner"
#
#     def scan(self, file_info):
#         if self.match_text is None:
#             raise ParameterNotMatchException("未指定扫描文本")
#         file_path = file_info.get("file_path")
#         image = Image.open(file_path)
#         parse_str = self.image_reader.readtext(image)
#         print(parse_str)
#         if not self.fuzzy_match:
#             if self.match_text in parse_str:
#                 return True
#             else:
#                 return False
#         else:
#             for line in parse_str:
#                 if fuzz.partial_ratio(line.strip("\n"), self.match_text) >= 80:
#                     return True
#             return False
#
#     def support_scan(self, file_info):
#         mime_type_enum = file_info.get("mime_type_enum")
#         match mime_type_enum:
#             case FileMimeTypeEnums.dwg | FileMimeTypeEnums.xcf | FileMimeTypeEnums.jpg | FileMimeTypeEnums.jpx | \
#                  FileMimeTypeEnums.png | FileMimeTypeEnums.apng | FileMimeTypeEnums.gif | FileMimeTypeEnums.webp | \
#                  FileMimeTypeEnums.cr2 | FileMimeTypeEnums.tif | FileMimeTypeEnums.bmp | FileMimeTypeEnums.jxr | \
#                  FileMimeTypeEnums.psd | FileMimeTypeEnums.ico | FileMimeTypeEnums.heic | FileMimeTypeEnums.avif:
#                 return True
#         return False
