"""
num = input("请输入一个数：")
def num_Abs(num):
    num = abs(int(num))
    return num
print("绝对值为：",num_Abs(num))
"""
import random
len = int(input("请输入验证码的长度："))
def verification_code_func(len):
    code_list = []
    for i in range(10):
        code_list.append(str(i))
    for i in range(65,91):
        code_list.append(chr(i))
    for i in range(97,123):
        code_list.append(chr(i))
    code = random.sample(code_list,len)
    global verification_code
    verification_code = ''.join(code)
    print("验证码为：",verification_code)
verification_code_func(len)
input_code = str(input("请输入验证码："))
while 1:
    if input_code == verification_code:
        print("验证成功！")
        break
    else:
        input_code = str(input("请重新输入验证码："))
        continue