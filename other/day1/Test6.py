# -*- coding: utf-8 -*-
class Hourse:
    color = "black"
class Donkey:
    age = 10

    #私有属性
    __agess = 100
    def __init__(self):
        print ("sing sing sing isng")
    def cry(self):
        print ("^^^^^^^^^^^^^^")

#继承
class Luozi(Hourse ,Donkey):
    def __init__(self):
        Donkey.__init__(self)
        print ("dace dace dace ")
    def add(self ,a ,b):
        print (a + b)
    #函数覆盖
    def cry(self):
        print ("1111111111111111111111111111111")

k = Luozi()
print (k.add(1 ,2))
k.cry()