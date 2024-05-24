import math
import os

import cchardet

from Expections.parameter_not_match_exception import ParameterNotMatchException
from Utils.file_mime_type_enums import FileMimeTypeEnums
from Utils.file_unit_enums import FileUnitEnums


def get_file_unit_size(file_path, unit):
    match_unit = None
    match unit:
        case FileUnitEnums.B | FileUnitEnums.KB | FileUnitEnums.MB | FileUnitEnums.GB | FileUnitEnums.TB:
            match_unit = True
    if not match_unit:
        raise ParameterNotMatchException("文件单位不规范，请输入<FileUnitEnums>类中所定义的格式")
    return convert_byte_2_unit(file_path, unit)


def decide_file_type_by_encode(file_path):
    file_type_dict = dict()
    with open(file_path, 'rb') as f:
        content = f.read(4096)  # 读取4096个字节，足以满足格式判断了。
        result = cchardet.detect(content)
        charset = result['encoding']
        confidence = result['confidence']

    if charset is not None and confidence > 0.9:
        file_type_dict["mime_type_enum"] = FileMimeTypeEnums.text
        file_type_dict["char_set"] = charset
        return file_type_dict
    file_type_dict["mime_type_enum"] = FileMimeTypeEnums.unknown
    file_type_dict["char_set"] = None
    return file_type_dict


def convert_byte_2_unit(file_path, unit):
    file_stats = os.stat(file_path)
    file_size_bytes = file_stats.st_size
    if unit == FileUnitEnums.B:
        return file_size_bytes
    return file_size_bytes / math.pow(1024, unit.value)


def resolve_file_path(file_path):
    dir_name, _ = os.path.splitext(file_path)
    file_base_name = os.path.basename(file_path)
    file_name_split = file_base_name.split(".")

    result = dict()
    result["full_file"] = file_path
    result["dir_name"] = dir_name
    result["full_name"] = file_base_name
    result["file_name"] = file_name_split[0]
    result["file_name_suffix"] = file_name_split[1]
    return result


