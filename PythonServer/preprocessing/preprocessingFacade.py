from preprocessing.nlp_preprocessing import NLPPreprocessing
from preprocessing.textExtractor import TextExtractor


class Preprocessor:
    def __init__(self):
        self.nlp_preprocessor = NLPPreprocessing()
        self.text_extractor = TextExtractor()

    def preprocessHtml(self, html_body):
        extracted = self.text_extractor.extract_all_text(html_body)
        preprocessed, raw_text = self.nlp_preprocessor.preprocess(extracted)
        length_check = [el for el in zip(preprocessed, raw_text) if len(el[0]) > 3]
        preprocessed, raw_text = [el[0] for el in length_check], [el[1] for el in length_check]
        return preprocessed, raw_text
