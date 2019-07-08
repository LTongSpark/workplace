# -*- coding: utf-8 -*-
#训练数据
import math
trainData =[
    (1,1,5),
    (1,2,3),
    (2,2,4),
    (2,3,5),
    (3,3,1),
    (3,4,3)
]

#总商品集合
items = [1,2,3,4,5,6,7,8,9,10]

#测试数据
testData1 =[
    (1,1,1),
    (1,2,2),
    (2,3,2),
    (2,4,3),
    (3,1,5)
]

#推荐数据
recData1 =[
    (1,1,1),
    (2,1,3),
    (3,2,3)
]

#推荐算法，计算用户u对商品i的评分
def recommRating(u, i):
    return 5
#评测准确度的函数
# U:user		, 用户
# I:Item		, 商品
# R:Rating	    , 评分
# T:Test		,测试数据集
# R:Rating      ,用户u对商品i的真实评分R
# R':Rating     ,推荐系统计算的用户u对商品i的预测评分R
# Test数据 :      元组集合(u1,i1,4)
#
############################
#		        ------------
#			   /---
#			2 /	\          2
#			 /	/  (R - R')
#		   \/	---
# RMSE =	 ------------------
#				T
#
#     方差法计算推荐系统准确度
############################
def rmse(testData):
    sum = 0
    for t in testData:
        sum = sum + math.pow(t[2] - recommRating(t[0],t[1]),2)
    return math.sqrt(sum)/len(testData)


############################
#          ----
#          \    |R - R'|
#          /
#          ----
# mae = -------------------
#		      T
#     绝对误差计算推荐系统准确度
############################

def mae(testDta):
    sum = 0
    for t in testDta:
        sum = sum + math.fabs(t[2] - recommRating(t[0],t[1]))
    return sum /len(testDta)
############################
# recall : 召回，命中的个数 / 实际商品数，理解为命中率。
#          推荐命中的商品数 / 用户实际交互的商品数.
#
#
#              ∑( Ru ∩ Tu)
# recall = -------------------
#		         Tu(测试集中所有用户观看影片的个数)
#     绝对误差计算推荐系统准确度
############################
def recall(recData, testData):
    count = getIntersects(recData, testData);
    return float(count) / len(testData)


############################
# precision : 准确率，命中的个数 / 推荐个数。
#
# Σ∏∩∪
#
#              ∑( Ru ∩ Tu)
# recall = -----------------------
#		         Ru(推荐商品数)
#     绝对误差计算推荐系统准确度
############################

def precision(recData ,testData):
    count = getIntersects(recData,testData);
    return float(count)/len(recData)

#计算推荐集和测试级的交集个数
def getIntersects(recData, testData):
    count = 0
    subtestdata = []
    for t in testData:
        subtestdata.append((t[0], t[1]))

    subrecdata = []
    for t in recData:
        subrecdata.append((t[0], t[1]))

    count = 0
    for t in subrecdata:
        if t in subtestdata:
            count += 1
    return count ;


##################################################
# 覆盖率 ： 推荐的商品个数占商品总数的比例。
#               U(Ru)      推荐的商品个数
# coverage =  ------------
#               I(总商品数)
##################################################

def coverage(recData,items):
    #set是不重复数据集
    s1 = set()
    for t in recData:
        s1.add(t[1])
    return float(len(s1)) /len(items)


##################################################
# 信息熵 ：经济学的术语，评判数据分布，值为0.5是一个极值。
#
# 信息熵 = -∑(relItemPop(i) * log relItemPop(i))
#
#
##################################################
def infoShang():
    #得到商品流行度字典
    itemPops = getItemPops(trainData)
    sum = 0
    for item in itemPops.values():
        #得到每个商品的流行度
        relPop = relIntmPop(item ,trainData)
        sum += relPop * math.log10(relPop)
    return -sum



##################################################
# 商品的流行度：计算某个商品的流行度。
#               在train中，某个商品购买的次数
#                   i购买次数
#p(i) = ----------------------------
#                 I(商品总数)
##################################################
def itemPop(itemID ,train):
    sum = 0
    for i in train:
        if i == itemID :
            sum += 1
    return sum
##################################################
# 商品的相对流行度：商品i的流行度 / 所有善品的流行度总和
#                   itemPop(i)
#票(i) = ----------------------------
#                 SUM(itemPop(i))
##################################################
def relIntmPop(itemID ,train):
    itemPops = getItemPops(train)
    #计算流行度总和
    itemPopSum = 0
    for v in itemPops.values():
        itemPopSum += v ;

    #取出善品item的流行度
    return float(itemPops[itemID]) / itemPopSum ;


##################################################
# 所有商品相对流行度字典,集合是dict{item->value}
##################################################

def getItemPops(train):
# 所有商品的流行度字典
    item_pops = {}
    for t in train:
        item = t[1]
        if item_pops.has_key(item):
            item_pops[item] = item_pops.get(item) + 1
        else:
            item_pops[item] = 1
    itemPopSum = 0
    for v in item_pops.values():
        itemPopSum += v ;
    return item_pops


##################################################
# 所有商品相对流行度集合
##################################################

def getRelItemPops(train):
    item_props = getItemPops(train)
    #计算流行度总和
    popSum = 0
    for key ,value in item_props.items():
        popSum += value

    #相对商品流行度字典
    rel_item_pops = {}
    for key ,value in item_props.items():
        rel_item_pops[key] = float(value) /popSum
    return rel_item_pops


##################################################
# 所有商品相对流行度有序List
##################################################
def getSortedRelItemPopList(train):
    rel_item_pops = getRelItemPops(train)
    rel_pops = rel_item_pops.values()
    result = sorted(rel_pops)
    return result


##################################################
# 基尼系数 ：衡量数据分布状况.
# p(i) : 是商品i的相对流行度,j是索引位置，将所有商品按照商品流行度进行排序，以1为基址。
# 基尼系数 = {∑(p(i) * (2 * j - n - 1))} / (n - 1)
#
##################################################

def gini(train):
    sortedPopList = getSortedRelItemPopList(train)
    index = 1
    sum = 0
    for v in sortedPopList:
        sum += (2*index -len(sortedPopList)-1)*v
        index+=1
    return sum / (len(sortedPopList) -1)


##################################################
# 多样性 ：推荐列表尽量涵盖用户的所有兴趣。反映的是推荐商品两两的不相似性。
#         和商品的相似度相对。
#         多样性是衡量推荐列表的指标。
#         针对一个用户的。
#                              ∑(s(i,j))
#    diversity =1 - -------------------------
#                       R(u)(R(u) - 1) / 2
##################################################
def diversity(userId, recData):
    simSum = 0
    # 提取推荐列表的所有商品
    recItems = []
    for t in recData:
        if t[0] == userId:
            recItems.append(t[1])

    index = 0
    while index < len(recItems) - 1:
        itemA = recItems[index]
        subindex = index + 1
        while subindex < len(recItems):
            itemB = recItems[subindex]
            # 累加商品相似度
            simSum += similarity(itemA, itemB)
            subindex += 1
        index += 1
    return 1 - (float(simSum) / (len(recItems) * (len(recItems) - 1) * 0.5))


##################################################
# 整体多样性 ：推荐列表中所有用户的多样性的平均值。
#
#    diversity =  1/U * ∑(diversity(u))
#
##################################################
def totalDiversity(recData):
    # 取出所有的不同用户
    users = set()
    for t in recData:
        users.add(t[0])

    # 计算所有用户多样性的总和
    diverSum = 0
    for u in users:
        diverSum += diversity(u, recData)

    return float(diverSum) / len(users);


################################################################################
# jaacard ：杰卡德相似度,用户u和v同时交互的商品个数 / 用户u和v交互商品个数的总和
#                  N(u) && N(v)
# jaacard =     -----------------
#                 N(u) || N(v)
################################################################################
def jaccardSim(itemsA, itemsB):
    # 计算共有商品数量
    common = 0
    for x in itemsA:
        if x in itemsB:
            common += 1

    if common == 0:
        return 0
    else:
        # 所有商品个数
        allItems = len(itemsA) + len(itemsB) - common
        return float(common) / allItems


################################################################################
# 余弦 ：  杰卡德相似度,用户u和v同时交互的商品个数 / 用户u和v交互商品个数的总和
#                       N(u) && N(v)
# cosSim =     ----------------------
#                   2 /-----------
#                    v N(u) * N(v)
################################################################################
def cosSim(itemsA, itemsB):
    # 计算共有商品数量
    common = 0
    for x in itemsA:
        if x in itemsB:
            common += 1
    if common == 0:
        return 0
    else:
        # 所有商品个数
        return float(common) / math.sqrt(len(itemsA) * len(itemsB))


#计算商品的相似度 ，两两商品之间的相似程度
def similarity(item1 ,item2):
    return 0.5
