from utils.constants import CACHE_PATH
from text_acquisition.quote_acquisition import get_quote
from text_acquisition.preloading import preload, update_preload, preload_exists


def load_text(content, seen, cache):
    if content == 'quotes':
        is_new = False
        try:
            quote, author, content = get_quote(seen)
            is_new = True
        except:
            quote, author = cache.pop()
            content = quote + author

        return quote, author, is_new

    
def load_cache():
    cache = preload() if preload_exists() else []
    
    return cache