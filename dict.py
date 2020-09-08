"""
userdata = {
    "admin": "123456",
    "default": "456789"
}
name = input("请输入用户名：")
if name in userdata:
    pwd = input("请输入密码：")
    if pwd == userdata[name]:
        print("密码正确")
    else:
        print("密码错误")
else:
    print("用户名错误!")

mylist = input("请输入一个字符串：")
count = {}
for i in mylist:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
print(count)
for x,y in count.items():
    print(x,y)
"""
name = "NIUZHE"
age = 21
work = "student"
dict = {}
dict[name] = age,work
for i in dict:
    print(i)
print(dict[name][0])
print(dict.values())