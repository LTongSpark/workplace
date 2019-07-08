from gensim import corpora, models


class TfidfModel(object):
    dictionary = None
    dic_dict_vector = []
    tfidf_model = None
    doc_tfidf_vector = []

    def createdict(self, doclist):
        self.dictionary = corpora.Dictionary(doclist)
        return sorted(list(self.dictionary.token2id.items()), key=lambda item: item[1]), self.dictionary.dfs

    def doc2bow(self, doc):
        tmp_vector = self.dictionary.doc2bow(doc)
        self.dic_dict_vector.append(tmp_vector)
        return tmp_vector

    def make_model(self, doc_dict_vector):
        self.tfidf_model = models.TfidfModel(doc_dict_vector)
        self.doc_tfidf_vector = self.tfidf_model[doc_dict_vector]
        return self.doc_tfidf_vector
