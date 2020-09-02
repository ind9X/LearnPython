"""
for i in "abcdefg":
    print("i is:", i)
"""
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
"""
"""
s = 0
for i in "12345":
    s = s + int(i)
    print(s)
"""
"""
s = 0
for i in range(1,101,2):
    s = s + i
    print(s)
"""
"""
s = 0
for i in range(1,10):
    if i % 3 == 0 or i % 5 == 0:
        s = s + i
print(s)
"""

import random
s = random.randint(1,100)
print(s)
while 1:
    num = input("请输入一个100以内的数字（5次机会）：").strip()
    if num.isdigit():
        num = int(num)
        times = 5
        i = 1
        while i < times:
            if num == s:
                print("恭喜你！用了%s次就猜对了！" % i)
                break
            elif num > s:
                print("很抱歉，猜的数字大了些，还有%s次机会" % (times - i))
                num = int(input("请重新输入："))
            else:
                print("很抱歉，猜的数字小了些，还有%s次机会" % (times - i))
                num = int(input("请重新输入："))
            i += 1
    

"""
num = input("请输入一个数：")
while not num.isdigit():
    num = input("请重新输入一个数：")
num = int(num)
while num > 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1
    print(num)
"""