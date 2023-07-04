import re
import string

double_quotes = [
    '“',
    '”',
    '«',
    '»',
    '„',
    '‟',
    '❝',
    '❞',
    '〝',
    '〞',
    '〟',
    '＂',
    ]

single_quotes = [
    '‘',
    '’',
]

def normalize_quotes(text: str) -> str:
    regex = r'(?:% s)' % '|'.join(double_quotes)
    text = re.sub(regex, '"', text)
    regex = r'(?:% s)' % '|'.join(single_quotes)
    text = re.sub(regex, "'", text)
    return text

def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""", '                                '))

def lowercase(text: str) -> str:
    return text.lower()