import json
import pickle

import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from risk_pro.knndata import KnnData

def read_json_info(file):
    with open(file,"r", encoding="utf-8") as rs:
        info = json.loads(rs)
    return info


def data_preproccess():
    #delim_whitespace = True:用空格分隔
    #index_col = 0:设置第1列数据作为index
    #header=None:没有每列的column name，自己设定
    f = open('D:/PyCharm/workplace/risk_pro/风险数据.txt')
    df_train = pd.read_table(f,header=None, encoding='utf-8',delim_whitespace=True,index_col=0)

    # 设置表头
    df_train.columns = ['风险', '进度', '预算', '范围']
    # print(df_train)
    #
    df_train_target = df_train["风险"].values
    df_train_data = df_train.drop("风险", axis=1).values
    print(df_train_target)
    print(df_train_data)
    cv=cross_validation.ShuffleSplit(df_train.shape[0], n_iter=1,test_size=0.2)
    # 1[80% ,20%]
    print(np.sum(df_train["风险"]==0))

    # smt=KnnData(df_train)
    # df_train_smt=pd.DataFrame(smt.over_sampling(),columns=df_train.columns)
    # df_train_target = df_train_smt["风险"].values
    # df_train_data = df_train_smt.drop("风险", axis=1).values
    # cv=cross_validation.ShuffleSplit(df_train_smt.shape[0], n_iter=1,test_size=0.2)


    # naive_bayes_classifier(cv,df_train_data,df_train_target)
    # knn_classifier(cv,df_train_data,df_train_target)
    logistic_regression_classifier(cv,df_train_data,df_train_target)
    random_forest_classifier(cv,df_train_data,df_train_target)
    # decision_tree_classifier(cv,df_train_data,df_train_target)
    # gradient_boosting_classifier(cv,df_train_data,df_train_target)
    # svm_classifier(cv,df_train_data,df_train_target)
    # svm_cross_validation(cv,df_train_data,df_train_target)

def decision_tree_classifier(cv,df_train_data,df_train_target):
    print("-----------决策树-----------")
    from sklearn import tree
    for train,test in cv:
        model = tree.DecisionTreeClassifier()
        model.fit(df_train_data, df_train_target)
    # print(svc.feature_importances_)
        print_score(model,df_train_data,df_train_target,train,test)

        # pickle.dump(model, open("model_save_file", 'wb'))
        # model=pickle.load(open("model_save_file", 'rb'))
        # test_x=pd.DataFrame(np.array([[1,14000,80]]))
        # print(model.predict(test_x))

def random_forest_classifier(cv,df_train_data,df_train_target):
    print("-----------随机森林-----------")
    from sklearn.ensemble import RandomForestClassifier
    for train,test in cv:
        model = RandomForestClassifier(n_estimators=3 ,max_depth=3).fit(df_train_data[train],df_train_target[train])
        # print(svc.feature_importances_)
        print_score(model,df_train_data,df_train_target,train,test)

        pickle.dump(model, open("model_save_file", 'wb'))
        # model=pickle.load(open("model_save_file", 'rb'))
        # test_x=pd.DataFrame(np.array([[1,14000,80]]))
        # print(model.predict(test_x))

# SVM Classifier
def svm_classifier(cv,df_train_data,df_train_target):
    print("-----------SVM-----------")
    from sklearn.svm import SVC
    for train,test in cv:
        model = SVC(kernel='rbf', probability=True)
        model.fit(df_train_data[train],df_train_target[train])
        print_score(model,df_train_data,df_train_target,train,test)

# GBDT(Gradient Boosting Decision Tree) Classifier 梯度提升树
def gradient_boosting_classifier(cv,df_train_data,df_train_target):
    print("-----------GBDT-----------")
    from sklearn.ensemble import GradientBoostingClassifier
    for train, test in cv:
        model = GradientBoostingClassifier(n_estimators=200)
        model.fit(df_train_data,df_train_target)
        print_score(model, df_train_data, df_train_target, train, test)

# SVM Classifier 交叉验证
def svm_cross_validation(cv,df_train_data,df_train_target):
    print("-----------SVM 交叉验证-----------")
    from sklearn.grid_search import GridSearchCV
    from sklearn.svm import SVC
    for train, test in cv:
        model = SVC(kernel='rbf', probability=True)
        param_grid = {'C': [1e-3, 1e-2, 1e-1, 1, 10, 100, 1000], 'gamma': [0.01, 0.001]}
        grid_search = GridSearchCV(model, param_grid,  verbose=2)    #
        grid_search.fit(df_train_data[train],df_train_target[train])
        best_parameters = grid_search.best_estimator_.get_params()
        # for para, val in list(best_parameters.items()):
        #     print(para, val)
        model = SVC(kernel='rbf', C=best_parameters['C'], gamma=best_parameters['gamma'], probability=True)
        model.fit(df_train_data[train],df_train_target[train])
        print_score(model, df_train_data, df_train_target, train, test)

def logistic_regression_classifier(cv,df_train_data, df_train_target):
    print("-----------Logistic Regression-----------")
    from sklearn.linear_model import LogisticRegression
    for train, test in cv:
        model = LogisticRegression(penalty='l2')
        model.fit(df_train_data, df_train_target)
        print_score(model, df_train_data, df_train_target, train, test)


def knn_classifier(cv,df_train_data, df_train_target):
    print("-----------KNN-----------")
    from sklearn.neighbors import KNeighborsClassifier
    for train, test in cv:
        model = KNeighborsClassifier(leaf_size=30,p=2,n_jobs=2)
        model.fit(df_train_data, df_train_target)
        print_score(model, df_train_data, df_train_target, train, test)

def naive_bayes_classifier(cv,df_train_data, df_train_target):
    print("-----------Multinomial Naive Bayes-----------")
    from sklearn.naive_bayes import MultinomialNB
    for train, test in cv:
        model = MultinomialNB(alpha=0.1)
        model.fit(df_train_data[train], df_train_target[train])
        print_score(model, df_train_data, df_train_target, train, test)

def print_score(model,df_train_data,df_train_target,train,test):
    print("score:{0:.3f},test score:{1:.3f}".format(
        model.score(df_train_data[train], df_train_target[train]),
        model.score(df_train_data[test], df_train_target[test]),
    ))
    predicted1 = model.predict(df_train_data[train])
    report1=classification_report(df_train_target[train],predicted1)
    print("train report:\n%s" % report1)
    predicted2 = model.predict(df_train_data[test])
    report2 = classification_report(df_train_target[test], predicted2)
    print("test report:\n%s" % report2)

if __name__ == '__main__':
    data_preproccess()