import re

def clean(text:str) -> str:
    text = text.replace("\\n", " ")
    text = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", text)
    text = text.replace("\'s", " \'s")
    text = text.replace("\'ve", " \'ve")
    text = text.replace("n\'t", " n\'t")
    text = text.replace("\'re", " \'re")
    text = text.replace("\'d", " \'d")
    text = text.replace("\'ll", " \'ll")
    text = text.replace(",", " , ")
    text = text.replace("!", " ! ")
    text = text.replace("(", " ( ")
    text = text.replace(")", " ) ")
    text = text.replace("?", " ? ")
    return text

def lowercase(text: str) -> str:
    return text.lower()

def contains_chatgpt_error(text:str) -> bool:
    if re.match(r"^[^A-Za-z0-9(),!?\'\`]*?ChatGPT Dec 15 Version\. Free Research Preview\. Our goal is to make AI systems more natural and safe to interact with\. Your feedback will help us improve\.\r\nNew chat(?:.|\s)*\r\nDark mode\r\nOpenAI Discord\r\nUpdates & FAQ\r\nLog out$", text):
        return True
    if re.match(r"^!\s*Only one message at a time\. Please allow any other responses to complete before sending another message, or wait one minute\.\s*There was an error generating a response", text):
        return True
    if re.match(r"^!(?:, |\s)*?network error(?:, |\s)*?There was an error generating a response", text):
        return True
    
    return False

def clean_chatgpt_output(text:str) -> str:
    text = re.sub(r"^!", "", text)
    text = re.sub(r"(?:\r\n)+Regenerate response", "", text)
    text = re.sub(r"(?:Contents may violate our content policy(?:\r\n)*)?This content may violate our content policy\. If you believe this to be in error, please submit your feedback \u2014 your input will aid our research in this area\.", "", text)
    text = re.sub(r"ChatGPT Dec 15 Version\. Free Research Preview\. Our goal is to make AI systems more natural and safe to interact with\. Your feedback will help us improve\.\r\nNew chat(?:.|\s)*\r\nDark mode\r\nOpenAI Discord\r\nUpdates & FAQ\r\nLog out$", "", text)
    return text