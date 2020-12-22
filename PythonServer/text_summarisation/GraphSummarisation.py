import numpy as np


class GraphTextSummary:

    def __init__(self, ngram_len=1):
        self.text_graph = None
        self.ngram_len = ngram_len
        self.graphs = []

    def make_graph(self, preprocessed_text, ngram_level):
        graph = {}
        tuple_size = ngram_level
        for idx in range(0, len(preprocessed_text) - tuple_size):
            try:
                graph[tuple(preprocessed_text[idx + k] for k in range(tuple_size))][
                    preprocessed_text[idx + tuple_size]] += 1
            except:
                try:
                    graph[tuple(preprocessed_text[idx + k] for k in range(tuple_size))].update(
                        {preprocessed_text[idx + tuple_size]: 1})
                except:
                    graph[tuple(preprocessed_text[idx + k] for k in range(tuple_size))] = {
                        preprocessed_text[idx + tuple_size]: 1}

        return graph

    def count_probability(self, list_of_tokens):
        if len(list_of_tokens) <= 1:
            return 0

        tuple_size = self.ngram_len
        scores = []
        for n_gram_level in range(1, self.ngram_len + 1):
            score = 0
            graph = self.graphs[n_gram_level - 1]
            for idx in range(len(list_of_tokens) - tuple_size):
                try:
                    score += 1 / graph[tuple(list_of_tokens[idx + k] for k in range(tuple_size))][
                        list_of_tokens[idx + tuple_size]]
                except Exception as e:
                    #                 print(str(e))
                    score += 1
            #         print("Score: ", score)
            #         print("len: ", len(list_of_tokens) - 1)
            scores.append(1 - score / (len(list_of_tokens) - 1))
        return np.mean(scores)

    def learn(self, preprocessed_full_text):
        for n_gram_level in range(1, self.ngram_len + 1):
            print(f"Learning {n_gram_level}")
            self.graphs.append(self.make_graph(preprocessed_full_text, n_gram_level))

    def summarize(self, preprocessed_text_lines, n_sentences=5, raw_text=None, ):
        scores = [(line, self.count_probability(line), idx) for idx, line in enumerate(preprocessed_text_lines)]
        sorted_scores = sorted(scores, key=lambda score: score[1], reverse=True)[:n_sentences]
        if not raw_text:
            lines_to_print = [el[0] for el in sorted(sorted_scores, key=lambda x: x[2])]
            # print("\n".join(' '.join(el) for el in lines_to_print))

        else:
            lines_to_print = [raw_text[el[2]] for el in sorted(sorted_scores, key=lambda x: x[2])]
            # print("\n".join(el for el in lines_to_print))
#         print("\n" . join(' '.join(el[0]) for el in sorted_scores[:n_sentences]))
#         out = "\n".join(' '.join(sorted_scores[:n_sentences]))
#         return out
        return lines_to_print
