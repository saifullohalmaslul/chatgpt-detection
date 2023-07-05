import re

def clean(string:str):
    string = string.replace("\\n", " ")
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = string.replace("\'s", " \'s")
    string = string.replace("\'ve", " \'ve")
    string = string.replace("n\'t", " n\'t")
    string = string.replace("\'re", " \'re")
    string = string.replace("\'d", " \'d")
    string = string.replace("\'ll", " \'ll")
    string = string.replace(",", " , ")
    string = string.replace("!", " ! ")
    string = string.replace("(", " ( ")
    string = string.replace(")", " ) ")
    string = string.replace("?", " ? ")
    return string

def lowercase(text: str) -> str:
    return text.lower()