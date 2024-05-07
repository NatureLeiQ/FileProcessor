import re


def get_unicode_decode(content):
    try:

        content = re.sub(r'(\\u[a-zA-Z0-9]{4})', lambda x: x.group(1).encode("utf-8").decode("unicode-escape"), content)
        return content
    except SyntaxError:
        return content
