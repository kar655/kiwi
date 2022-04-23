import re
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


def clean_sentence(sentence: str) -> str:
    sentence = sentence.lower()
    stop_words = set(stopwords.words('english'))
    # Change words to their basic form.
    stemmer = PorterStemmer()

    # Removes @, # and links.
    sentence = re.sub("@\S+", "", sentence)
    sentence = re.sub("https?:\/\/.*[\r\n]*", "", sentence)
    sentence = re.sub("#", "", sentence)

    # Skip stop words and punctuation.
    cleaned = [word for word in sentence.split()
               if word not in stop_words
               and word not in string.punctuation]

    return " ".join(cleaned)
