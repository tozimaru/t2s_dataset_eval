import os

CYRIL_ENG_DICT = {
    'а': 'a',
    'ә': 'e',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'ye',
    'ё': 'yo',
    'ж': 'j',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'ө': 'ö',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ү': 'ü',
    'ф': 'f',
    'х': 'kh',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'shch',
    'ъ': '',
    'ы': 'y',
    'ь': 'i',
    'э': 'e',
    'ю': 'yu',
    'я': 'ya',    
}

#having a transliterator is useful when we want to train a vocoder with an english corpus as an addition
def cyrillic_to_eng(text, lookup_dict):
    english_text = ''
    for letter in text:
        english_text += lookup_dict.get(letter.lower(), letter)
    return english_text    