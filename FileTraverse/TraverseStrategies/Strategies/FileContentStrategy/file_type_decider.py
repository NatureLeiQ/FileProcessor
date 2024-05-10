# import magic
import os

import cchardet
import filetype

from Utils.file_mime_type_enums import FileMimeTypeEnums


class FileTypeDecider:
    # 文件类型判定器
    def __init__(self):
        pass

    def decide_file_type(self, file_path):
        """
        三步走：先用guess判断文件类型，再用文件后缀判断，若最后都没得到结果，那就用cchardet进行编码判断。目前只支持utf-8格式的
        :return FileMimeTypeEnums和编码。编码是可选的，因为有个是一类，比如说文本文件，就含有编码。而pdf，jpg这种格式是固定的，但是文本文件是根据编码区分的
        """
        # 三方库判断
        file_type_dict = dict()
        kind = filetype.guess(file_path)
        if kind is not None:
            mime_type = FileMimeTypeEnums.get_enum_by_value(kind.mime)
            if mime_type != FileMimeTypeEnums.unknown:
                file_type_dict["mime_type_enum"] = mime_type
                file_type_dict["char_set"] = None
                return file_type_dict

        # 后缀判断
        # file_extension = self._get_file_extension(file_path)
        # mime_type = FileMimeTypeEnums.get_enum_by_value(file_extension)
        # if mime_type != FileMimeTypeEnums.unknown:
        #     return mime_type

        # 文件编码判断
        charset, confidence = self._detect_encoding(file_path)
        if charset is not None and confidence > 0.9:
            file_type_dict["mime_type_enum"] = FileMimeTypeEnums.text
            file_type_dict["char_set"] = charset
            return file_type_dict

        return FileMimeTypeEnums.unknown

    @staticmethod
    def _detect_encoding(file_path):
        with open(file_path, 'rb') as f:
            content = f.read(4096)  # 读取4096个字节，足以满足格式判断了。
            result = cchardet.detect(content)
            charset = result['encoding']
            confidence = result['confidence']
            return charset, confidence

    @staticmethod
    def _get_file_extension(file_path):
        base, extension = os.path.splitext(file_path)
        extension_without_dot = extension[1:] if extension else None
        return extension_without_dot


