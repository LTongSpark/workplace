#-*-encoding:utf-8-*-

def read_join():
    base_dir = "D:/mr"

    with open(base_dir + '/json.txt', 'r') as f:
        json_list = f.read().replace('\r', '').replace('\n', ',').split(',')

    with open(base_dir + '/scores.txt', 'r') as f:
        scores_list = f.read().replace('\r', '').replace('\n', ',').split(',')

    with open(base_dir+'/words.txt', 'w+') as f:
        for index in zip(scores_list, json_list):
            f.write(index[0]+"\t\t" +index[1] + "\r")

# phoneNum = open(r'/home/oycm/shuju/phoneNum.txt', 'w')
# if_black = open(r'/home/oycm/shuju/if_black.txt', 'w')
# base_dir = "/home/oycm/shuju"
#
# with open(base_dir + '/static_phoneNum.txt', 'w+') as f:
#     for i in x_test["phone_no"].values:
#         f.write(str(i) + "\r")

# with open(base_dir + '/static_if_black.txt', 'w+') as f:
#     for i in y_predict:
#         f.write(str(i) + "\r")
# # print("准确率：", lg.score(x_test1, y_test))
# with open(base_dir + '/static_phoneNum.txt', 'r') as f:
#     json_list = f.read().replace('\r', '').replace('\n', ',').split(',')
#
# with open(base_dir + '/static_if_black.txt', 'r') as f:
#     scores_list = f.read().replace('\r', '').replace('\n', ',').split(',')
#
# with open(base_dir + '/static_result.txt', 'w+') as f:
#     for index in zip(scores_list, json_list):
#         f.write(index[0] + "\t\t" + index[1] + "\r")