#-*-encoding:utf-8-*-
list1 = open("D:\mr\scores.txt" ,"r")
base_dir = "D:/mr"
json_dir = base_dir + '/json.txt'
scores_dir = base_dir + '/scores.txt'

with open(json_dir, 'r') as f:
    json_list = f.read().replace('\r', '').replace('\n', ',').split(',')

with open(scores_dir, 'r') as f:
    scores_list = f.read().replace('\r', '').replace('\n', ',').split(',')

for index in zip(scores_list, json_list):
    print(index[0], index[1])



