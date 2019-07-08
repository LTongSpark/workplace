#-*-encoding:utf-8-*-
import pandas as pd
data_black = pd.read_excel("C:/Users/Administrator/Desktop/19研判处置号码库4月22日.xlsx")
readDir = "C:/Users/Administrator/Desktop/result.txt"
f = open(readDir ,"r" ,encoding="utf-8")
list_num = [i.replace("\n" ,"") for i in f]
result_phone = set()
phone_black = data_black["号码"]
phone_black.fillna(value=0, inplace=True)
for phone_num in phone_black:
    for modle_num in list_num:
        if (int(modle_num) == int(phone_num)):
            result_phone.add(phone_num)
print("percent : {:.1f}%".format(len(result_phone)/len(set(list_num))*100))
