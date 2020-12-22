from preprocessing.preprocessingFacade import Preprocessor
from text_summarisation.GraphSummarisation import GraphTextSummary


class ImportantThingsExtractor:

    def __init__(self):
        self.preprocessing = Preprocessor()

    def extract(self, html_body: str) -> list:
        algorithm = GraphTextSummary(2)
        preprocessed, raw_text = self.preprocessing.preprocessHtml(html_body)
        algorithm.learn([el for line in preprocessed for el in line])
        number_of_sentences = int(0.2*len(preprocessed)) + 1
        important_things = algorithm.summarize(preprocessed, number_of_sentences, raw_text)
        return important_things
