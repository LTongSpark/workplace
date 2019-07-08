# -*-encoding:utf-8-*-
import pandas as pd

result_file = "C:/Users/Administrator/Desktop/数据结果20190302.txt"
black_file = "D:/google/19年研判处置关停号码库0303.xlsx"

f = open(result_file,encoding="utf-8")
data_black = pd.read_excel(black_file, sheetname=0)
data = pd.read_csv(f, header=None ,encoding="utf-8")
# 模型数据
modle_data = set()
result_phone = set()

# 模型跑出来的数据
data[0] = data[0].str.replace(" ","")
data["phone_no"] = data[0].str.split("|", expand=True)[1]
data["c_cust_cert_code"] = data[0].str.split("|", expand=True)[2]
data["city_code"] = data[0].str.split("|", expand=True)[3]
data["rome_city_code"] = data[0].str.split("|", expand=True)[4]
data["stat_date"] = data[0].str.split("|", expand=True)[5]
del data[0]

for phone in data["phone_no"]:
    modle_data.add(phone)

phone_black = data_black["号码"]
phone_black.fillna(value=0, inplace=True)
for phone_num in phone_black:
    for modle_num in modle_data:
        if (int(modle_num) == int(phone_num)):
            result_phone.add(phone_num)

# 把黑名单从新作为索引
data_black = data_black.set_index("号码", drop=False)
data = data.set_index("phone_no" ,drop=False)
data = data.drop_duplicates("phone_no")

print(data.duplicated())

for modle_phone in modle_data:
    for result_data in result_phone:
        if(int(modle_phone) == int(result_data)):
            print((str(int(float(modle_phone)))) + "\t" * 2 +
              data.loc[str(modle_phone), "c_cust_cert_code"] + "\t" *2 +
              data.loc[str(modle_phone), "city_code"] + "\t" * 2 +
              data.loc[str(modle_phone), "rome_city_code"] + "\t" * 2 +
              data.loc[str(modle_phone), "stat_date"] + "\t" * 2 +
              str(int(float(data_black.loc[int(modle_phone), "关停时间"])))
              +str(data_black.loc[int(modle_phone), "关停原因"]))
            break
    else:
        print((str(int(float(modle_phone)))) + "\t" * 2 +
              data.loc[str(modle_phone), "c_cust_cert_code"] + "\t" * 2 +
              data.loc[str(modle_phone), "city_code"] + "\t" * 2 +
              data.loc[str(modle_phone), "rome_city_code"] + "\t" * 2 +
              data.loc[str(modle_phone), "stat_date"] + "\t" * 2)



