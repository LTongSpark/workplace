#-*-encoding:utf-8-*-

import re
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

class DataClean:
    @staticmethod
    def lower(doc_str):
        return doc_str.strip().lower()
    @staticmethod
    def remove_special_char(doc_str, special_char=None):
        spchar = re.findall(u"[－＝＿＋～｀＾！＊€§·◦•●＠＃￥＄％＆？．，。：；、…（）［］【】＜＞｛｝/`'’]+", doc_str)
        doc_str = re.sub(u"[－＝＿＋～｀＾！＊€§·◦•●＠＃￥＄％＆？．，。：；、…（）［］【】＜＞｛｝/`'’]+", " ", doc_str)
        if special_char:
            spchar += re.findall(u"[" + re.escape(special_char) + "]+", doc_str)
            doc_str = re.sub(u"[" + re.escape(special_char) + "]+", " ", doc_str)
        return doc_str, spchar

    @staticmethod
    def word_tokenize(doc_str):
        text_tokenized = [word for word in word_tokenize(doc_str)]
        return text_tokenized

    @staticmethod
    def stop_word(texts_tokenized):
        english_stopwords = list(ENGLISH_STOP_WORDS)
        texts_filtered_stopwords = [word for word in texts_tokenized if word not in english_stopwords]
        stopwords = [word for word in texts_tokenized if word in english_stopwords]
        return texts_filtered_stopwords, stopwords

    @staticmethod
    def remove_punctuation(words_list):
        english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!',
                                '*', '@', '#', '$', '%', '{', '}', '-', '\'', '`', '/',
                                '+', '-', '<', '>']
        texts_filtered = [word for word in words_list if word not in english_punctuations]
        texts_punctuations = [word for word in words_list if word in english_punctuations]
        return texts_filtered, texts_punctuations

    @staticmethod
    def word_trans(texts_filtered, word_type="wordstem"):
        if word_type == "wordstem":
            st = PorterStemmer()
            texts_stemmed = [st.stem(word) for word in texts_filtered]
        elif word_type == "wordnet":
            wnl = WordNetLemmatizer()
            texts_stemmed = [wnl.lemmatize(word) for word in texts_filtered]
        return texts_stemmed

    @staticmethod
    def special_words(texts_stemmed, special_words=None):
        if special_words:
            texts_specialed = [word for word in texts_stemmed if word not in special_words]
            specialwords = [word for word in texts_stemmed if word in special_words]
        else:
            texts_specialed = texts_stemmed
            specialwords = []
        return texts_specialed, specialwords


class KeyWordsExtractor(object):

    def __init__(self, keywords=None):
        keywords = keywords or []
        self.keywords = keywords
        self.l_keyword_regex = [(keyword.lower(), re.compile("\W(%s)\W" % re.escape(keyword.lower().strip()))) for
                                keyword in keywords]

    def extract_keywords(self, doc):
        """ 提取关键字，返回剩余的部分以及关键字"""
        if not doc:
            return "", []
        rv = []
        tmp_doc = doc.lower()

        try:
            # 找出在文档中存在的关键字
            l_keyword_regex = [keyword_regex for keyword_regex in self.l_keyword_regex if
                               keyword_regex[1].search(" " + tmp_doc + " ")]
            #
            for i, keyword_regex in enumerate(l_keyword_regex):
                rv.extend(keyword_regex[1].findall(" " + tmp_doc + " "))
                tmp_doc = keyword_regex[1].sub(" ", " " + tmp_doc + " ")
        except Exception as e:
            print(e)
        return tmp_doc.strip(), rv
