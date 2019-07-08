#-*-encoding:utf-8-*-

product_list = [
    ("apple",12),
    ("tree",14),
    ("arr",23),
    ("we",13)
]

shopping_list = []
salary = input("please input my scalay:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index ,item in enumerate(product_list):
            print(index ,item)
        user_choice = input("please choice shopping :")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice<len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1]<salary and p_item[1] >=0:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" % (p_item, salary))
                else:
                    print("你的余额不足剩余%s" %salary)
            else:
                print("输入的商品不合法")
        elif user_choice == "q":
            for i  in shopping_list:
                print(i)
                exit()
        else:
            print("invilid producet")

