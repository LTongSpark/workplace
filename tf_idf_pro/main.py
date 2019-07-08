# -*- coding: utf-8 -*-
from tf_idf_pro.textproc import KeyWordsExtractor, DataClean
from tf_idf_pro.tfidf_model import TfidfModel
from tf_idf_pro.sim_model import SimilarityModel

corpus_content = [
    (0,
     """The Chinese auto industry attracted much attention at the ongoing two sessions in Beijing, as top policymakers discussed a wide range of issues from new-energy vehicles (NEVs) to autonomous driving to the development of domestic brands."""),
    (1,
     """US President Donald Trump on Friday signed the so-called "Taiwan Travel Act," which aims to encourage visits between US and Taiwan functionaries at all levels, according to the White House."""),
    (2,
     """Fifty years after taking photos of an American massacre of Vietnamese villagers, a former US army photographer said he is sorry for the "carnage" his countrymen unleashed in one the war's worst atrocities."""),
    (3,
     """Moscow vowed Friday to hit back at Britain with its own raft of punitive measures "any minute" after the West blamed Russia directly for a nerve agent attack on a former double agent."""),
    (4,
     """A North Korean envoy began a visit to Sweden amid speculations about the venue of the announced meeting between North Korean leader Kim Jong-un and US President Donald Trump."""),
    (5,
     """Seventeen men who enlisted then quit the army have been sent home and blacklisted on China's social credit system, according to a notice released on Thursday that listed all their names and addresses. """),
    (6,
     """In the largest exercise of its kind, more than 10,000 troops traveled more than 2,000 kilometers to arrive on Monday at two army training bases in Southwest China's Yunnan Province and East China's Shandong Province and begin battle training, China Central Television show Military Report reported. """),
    (7,
     """The US state of Alaska is getting one step closer to Chinese investments in its ambitious energy program after US energy regulators began assessing a planned liquefied natural gas (LNG) project in the state."""),
    (8,
     """The communication channels between China and the Vatican are necessary and must be enhanced over the severe bishop shortage in China's Catholic parishes, a bishop warned Thursday. """),
    (9,
     """A Chinese －＝ firm has broken developed countries' corporate stranglehold on ultra-large shield tunneling equipment with a contract to export China's largest tunneling machine. """)
]

def to_lower(corpus):
    return [(i, content.lower()) for i, content in corpus]


def print_rv(rv):
    for item in rv:
        print(item)


def get_top_n(query, top_n=3):
    rv = query.lower()
    rv, key_words = kw.extract_keywords(rv)
    remain_doc, _ = DataClean.remove_special_char(rv)
    rv = DataClean.word_tokenize(remain_doc)
    rv, _ = DataClean.remove_punctuation(rv)
    rv, stop = DataClean.stop_word(rv)
    rv = DataClean.word_trans(rv)
    rv += key_words
    rv = tfidf.doc2bow(rv)
    rv = tfidf.tfidf_model[rv]
    rv = model.model[rv]
    model.index.num_best = top_n
    rv = model.index[rv]
    print(rv)


if __name__ == '__main__':
    # 转小写
    lower_rv = to_lower(corpus_content)
    # print_rv(lower_rv)

    # 提取关键词
    kw = KeyWordsExtractor(["Vietnamese villagers"])
    kw_rv = []
    for i, doc in lower_rv:
        remain_doc, key_words = kw.extract_keywords(doc)
        kw_rv.append((i, remain_doc, key_words))

    # print_rv(kw_rv)

    # 去除特殊字符
    rm_special_rv = []
    temp = []
    for i, doc, key_words in kw_rv:
        remain_doc, rm_special = DataClean.remove_special_char(doc)
        if rm_special:
            temp.append(rm_special)
        rm_special_rv.append((i, remain_doc, key_words))

    # print_rv(rm_special)
    # print_rv(rm_special_rv)

    # 分词
    tokenize_words = []
    for i, doc, key_words in rm_special_rv:
        tokenize_words.append(DataClean.word_tokenize(doc))

    # print_rv(tokenize_words)

    # 去除标点符号
    rm_punc_rv = []
    punc_rv = []
    for words in tokenize_words:
        rv, puncs = DataClean.remove_punctuation(words)
        punc_rv.append(puncs)
        rm_punc_rv.append(rv)

    # print_rv(punc_rv)
    # print_rv(rm_punc_rv)

    # 去停用词
    rm_stopword_rv = []
    stop_words = []
    for words in rm_punc_rv:
        rv, stop = DataClean.stop_word(words)
        rm_stopword_rv.append(rv)
        stop_words.append(stop)

    # print_rv(stop_words)
    # print_rv(rm_stopword_rv)

    # 词干化
    rm_stem_rv = []
    for words in rm_stopword_rv:
        rv = DataClean.word_trans(words)
        rm_stem_rv.append(rv)
    # print_rv(rm_stem_rv)

    # 合并关键词
    final_rv = []
    for i, item in enumerate(kw_rv):
        final_rv.append((i, rm_stem_rv[i] + item[2]))

    # print_rv(final_rv)

    # 建立词典
    tfidf = TfidfModel()
    documents = [item[1] for item in final_rv]
    rv = tfidf.createdict(documents)
    # print(tfidf.dictionary)

    # 建立词袋模型
    bow = []
    for doc in documents:
        bow.append(tfidf.doc2bow(doc))
    # print_rv(bow)

    # 建立TFIDF模型
    tfidf_vectors = tfidf.make_model(bow)
    # print_rv(tfidf_vectors)

    # 建立主题模型
    model = SimilarityModel()
    rv = model.make_model(tfidf_vectors, "lsi", tfidf.dictionary, 10)
    # print_rv(rv)

    rv = model.make_index(tfidf_vectors)
    print(rv.index)

    # 推荐
    rv = get_top_n("The Chinese auto industry attracted much attention at the ongoing tw")





