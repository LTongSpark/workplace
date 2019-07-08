# -*- coding: utf-8 -*-
import pandas as pd

class percent(object):
    def __init__(self):
        self.black_path = "C:/Users/Administrator/Desktop/19研判处置号码库.xlsx"
        self.result = "C:/Users/Administrator/Desktop/result-5.31-6.06.txt"
        self.result_phone = set()
    def run(self):
        data_black = pd.read_excel(self.black_path)
        result_num = [i.replace("\n" ,"") for i in open(self.result ,"r" ,encoding="utf-8")]
        phone_black = data_black["号码"]
        print(phone_black)
        phone_black.fillna(value=0, inplace=True)
        for phone_num in phone_black:
            for modle_num in result_num:
                if (int(modle_num) == int(phone_num)):
                    self.result_phone.add(phone_num)

        return "percent : {:.1f}%".format(len(self.result_phone) / len(set(result_num)) * 100)

if __name__ == '__main__':
    percent = percent().run()
    print(percent)