import nltk
nltk.download('punkt')
nltk.download('punkt_tab')   # IMPORTANT Fix

from nltk.tokenize import word_tokenize

sentence = "I love NLP and Python!"
tokens = word_tokenize(sentence)

print(tokens)
