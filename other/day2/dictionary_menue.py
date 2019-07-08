# -*-encoding:utf-8-*-
data = {
    '北京': {
        "昌平": {
            "沙河": ["oldboy", "test"],
            "天通苑": ["链家地产", "我爱我家"]
        },
        "朝阳": {
            "望京": ["奔驰", "陌陌"],
            "国贸": {"CICC", "HP"},
            "东直门": {"Advent", "飞信"},
        },
        "海淀": {},
    },
    '山东': {
        "德州": {},
        "青岛": {},
        "济南": {}
    },
    '广东': {
        "东莞": {},
        "常熟": {},
        "佛山": {},
    },
}
while True :
    for i in data:
        print(i)
    choice = input("选择进入>>>>1")
    if choice in data:
        while True:
            for i1 in data[choice]:
                print("\t",i1)
            choice2 = input("选择进入>>>2")
            if choice2 in data[choice]:
                while True:
                    for i2 in data[choice][choice2]:
                        print("\t\t",i2)
                    choice3 = input(">>>>3")
                    if choice3 in data[choice][choice2]:
                        for i3 in data[choice][choice2][choice3]:
                            print(i3)

