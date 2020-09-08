"""
#h = open("test.txt","a")
h = open("test.txt","w")
h.write("Hello World!")
h = open("test.txt","r")
print(h.read())
h.close()

with open("test.txt","r") as h:
    print(h.read())
"""
"""
with open("KMSWHS.txt","r") as s:
    s = str(s.read())
    count = {}
    for i in s:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    for x,y in count.items():
        print(x,y)
    print(count)
"""
"""
def Home():
    num = input("请选择：1.注册     2.登录     ")
    if num == "1":
        Signup()
    elif num == "2":
        Login()
    else:
        print("选择有误！请重新选择。")
        Home()
"""

def Signup():
    print("请先注册您的账户！")
    userdatadict = {}
    FileToDict(userdatadict)
    name = input("请输入您的用户名：").strip()
    while name in userdatadict:
        name = input("您的用户名已存在，请重新输入您的用户名：").strip()
    while len(name) != 0 and len(name) <= 3 or len(name) > 9:
        name = input("您的用户名长度不符合规则，请重新输入您的用户名：").strip()
    pwd = input("请输入您的密码：").strip()
    while 5 >= len(pwd) or len(pwd) > 10:
        pwd = input("您的密码长度不符合规则，请重新输入您的密码：").strip()
    DictToFile(name,pwd)
    print("注册成功，请登录！")
    Login()

def Login():
    userdatadict = {}
    FileToDict(userdatadict)
    username = input("请输入用户名：")
    if username in userdatadict:
        userpwd = input("请输入您的密码：")
        if userpwd == userdatadict[username]:
            print("登录成功")
        else:
            i = 0
            for i in range(3):
                userpwd = input("密码错误！请重新输入您的密码：")
                if userpwd == userdatadict[username]:
                    print("登录成功！")
                    break
                i += 1
                if i == 2:
                    print("您的三次机会已经用完，请重头开始！")
                    Locked()
    else:
        print("您的用户不存在，将自动前往注册")
        Signup()

def Locked():
    print("您的三次机会已用完，程序已锁定，请使用管理员账户解锁！")
    while 1:
        adminname = input("请输入您的管理员账户：")
        if adminname.strip() == "admin":
            adminpwd = input("请输入您的管理员密码：")
            if adminpwd == "123456":
                print("解锁成功！请重新前往注册！")
                Signup()
            else:
                print("密码错误")
                continue
        else:
            print("您的管理员账户出错！")
            continue

def DictToFile(name,pwd):
    datadict = {}
    datadict[name] = pwd
    with open("userdata.txt", "a") as data:
        for name,pwd in datadict.items():
            data.write(str(name) + '     ' + str(pwd) + '' + '\n')

def FileToDict(userdatadict):
    with open("userdata.txt","r") as userdata:
        for line in userdata.readlines():
            line = line.strip()
            name = line.split('     ')[0]
            pwd = line.split('     ')[1]
            userdatadict[name] = pwd
        return userdatadict

#Home()
Signup()