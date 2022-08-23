from utils.constants import PRELOAD_BUFFER
from text_acquisition.quote_acquisition import get_quote
from text_acquisition.preloading import preload, update_preload, preload_exists

def load_text(content, seen):
    if content == 'quotes':
        if preload_exists():
            data = preload()
            for quote, _ in data:
                seen.add(quote)
            return data 
        quote, author = get_quote(seen)
        return [[quote, author]]