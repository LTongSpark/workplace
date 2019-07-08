# -*- coding: utf-8 -*-


from gensim import models, similarities


class SimilarityModel(object):
    dictionary = None
    doc_dict_vector = []
    dic_tfidf_vector = []

    model_cls = None
    topics_num = None
    model_type = None
    model = None

    def make_model(self, corpus, model_type, dictionary, topics_num):

        if model_type == "lsi":
            self.model_cls = models.LsiModel
        elif model_type == "lda":
            self.model_cls = models.LdaModel

        self.topics_num = topics_num
        self.model_type = model_type

        self.model = self.model_cls(corpus, id2word=dictionary, num_topics=int(topics_num))
        temp_model = self.model.print_topics(num_words=20, num_topics=int(topics_num))
        return temp_model

    def make_index(self, corpus):
        self.index = similarities.MatrixSimilarity(self.model[corpus])
        return [
            [round(float(k), 4) for k in str(item).strip("[").strip("]").split(" ") if k != ""
             ] for item in self.index.index
                ]
