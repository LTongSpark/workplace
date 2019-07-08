#-*-encoding:utf-8-*-
import jieba

s1 = "这只皮靴号码大了。那只号码合适"
s2 = "这只皮靴号码不小，那只更合适"

s1_seg = '/'.join([x for x in jieba.cut(s1, cut_all=True) if x != ''])
s1_lst = [x for x in jieba.cut(s1, cut_all=True) if x != '']
s1_set = set(s1_lst)

s2_seg = '/'.join([x for x in jieba.cut(s2, cut_all=True) if x != ''])
s2_lst = [x for x in jieba.cut(s2, cut_all=True) if x != '']
s2_set = set(s2_lst)

word_dict = dict()
i = 0
for word in s1_set.union(s2_set):
    word_dict[word] = i
    i += 1


def word_to_vec(word_dict, s1_lst):
    word_count1 = dict()
    # 建立一个数组为字典长度，元素的值全为0的数组
    s1_vector = [0] * len(word_dict)
    for word in s1_lst:
        #取不到值就是-1
        if word_count1.get(word, -1) == -1:
            word_count1[word] = 1
        else:
            word_count1[word] += 1
    # print(word_count1)

    for word, freq in word_count1.items():
        wid = word_dict[word]
        s1_vector[wid] = freq
    # print(s1_vector)
    return s1_vector


s1_vector = word_to_vec(word_dict, s1_lst)
print(s1_vector)
s2_vector = word_to_vec(word_dict, s2_lst)
print(s2_vector)


# print(s1_seg)
# print(s2_seg)

