
def ten_24(num):
    loop = '0123456789abcdefghijklmnopqrstuvwxyz'
    a = []
    while num != 0:
        a.append(loop[int(num) %24])
        num = int(num /24)
    a.reverse()
    return ''.join(a).upper()


print(ten_24(128113))



print(int('hqoh9yhz', 36))
print(int('96A1', 24))
print('*'*20)
print(int('24083', 24))
print(int('54810', 24))