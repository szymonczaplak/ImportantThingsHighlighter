import re

import nltk.data
from tensorflow.keras.preprocessing.text import text_to_word_sequence
import spacy

class NLPPreprocessing:
    def __init__(self):
        self.tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        self.nlp = spacy.load('en_core_web_sm')

    def preprocess(self, org_text):
        text = re.sub('\.', '. ', org_text)
        text = re.sub('\!', '! ', text)
        text = re.sub('\?', '? ', text)
        text_lines = self.tokenizer.tokenize(text)
        # tokenized_lines = [text_to_word_sequence(line) for line in text_lines]
        # text_doc = self.nlp(text_lines)

        tokenized_lines = [
            [token.text for token in self.nlp(line)
                 if not token.is_stop and not token.is_punct]
        for line in text_lines]



        return tokenized_lines, text_lines
