import nltk.data
from tensorflow.keras.preprocessing.text import text_to_word_sequence


class NLPPreprocessing:
    def __init__(self):
        self.tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    def preprocess(self, text):
        text_lines = self.tokenizer.tokenize(text)
        tokenized_lines = [text_to_word_sequence(line) for line in text_lines]
        return tokenized_lines, text_lines
