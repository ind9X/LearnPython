# 1
"""
num1 = input("请输入被除数：")
while 1:
    try:
        num1 = int(num1)
    except ValueError:
        num1 = input("请重新输入被除数：")
        continue
    else:
        num2 = input("请输入除数：")
        while 1:
            try:
                num2 = int(num2)
            except ValueError:
                num2 = input("请重新输入除数：")
                continue
            else:
                try:
                    num3 = int(num1) / int(num2)
                except ZeroDivisionError:
                    num2 = input("除数不能为零，请重新输入除数：")
                    continue
                else:
                    num3 = int(num1) / int(num2)
                    break
    break
print(num1, '/', num2, '= %.2f' % num3)
"""
# 2
with open('userdata.txt', 'r') as file:
    num = 1 / 0
    print(file.read())