import pathlib
from fuzzywuzzy.fuzz import token_sort_ratio

def parse_url_keywords(config_dir):
    file_content = None
    with open(config_dir + '/url_rank.cfg', 'r') as f:
        file_content = f.read()

config_dir = pathlib.exec_dir + '/config'
url_keywords = parse_url_keywords(config_dir)
slash_range = (2, 5)

def url_score(url):
    return 0

def rank_result(result, keyword):
    ratio = token_sort_ratio(str(result), keyword)
    url = url_score(result.url)
    return (ratio * 0.7) + (url * 0.3)
