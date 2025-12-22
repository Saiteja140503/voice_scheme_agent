from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def to_telugu(text):
    return transliterate(text, sanscript.DEVANAGARI, sanscript.TELUGU)
