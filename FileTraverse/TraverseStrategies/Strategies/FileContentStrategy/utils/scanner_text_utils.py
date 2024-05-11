from fuzzywuzzy import fuzz


def content_match(content, match_text, fuzzy_match):
    if not fuzzy_match:
        if match_text in content:
            return True
        else:
            return False
    else:
        if fuzz.partial_ratio(content.strip("\n"), match_text) >= 80:
            return True
        return False
