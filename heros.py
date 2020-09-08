import math
import random
import sys

def Home():
    num = input("欢迎来到Heros World！请选择：1.注册     2.登录     ")
    if num == "1":
        Signup_name()
    elif num == "2":
        Login()
    else:
        print("选择有误！请重新选择。")
        Home()

def Signup_name():
    userdatadict = {}
    FileToDict(userdatadict)
    print("#" * 50)
    print("欢迎来到Heros World！注册界面")
    name = input("请输入您的用户名：").strip()
    while len(name) != 0 and len(name) <= 3 or len(name) > 9:
        name = input("您的用户名长度不符合规则，请重新输入您的用户名：").strip()
    while name in userdatadict:
        name = input("用户名已存在！请重新输入：").strip()
        while len(name) != 0 and len(name) <= 3 or len(name) > 9:
            name = input("您的用户名长度不符合规则，请重新输入您的用户名：").strip()
    if not name:
        name = 'player' + str(random.randrange(101,199))
        print("检测到您未输入用户名，我们将随机生成一个您的用户名：",name)
        Signup_pwd(name)
    else:
        Signup_pwd(name)

def Signup_pwd(name):
    pwd = input("请输入您的密码：").strip()
    while 5 >= len(pwd) or len(pwd) > 10:
        pwd = input("您的密码长度不符合规则，请重新输入您的密码：").strip()
    print("注册成功，请返回主页面登录！")
    DictToFile(name,pwd)
    Home()

def Login():
    userdatadict = {}
    FileToDict(userdatadict)
    username = input("请输入您的用户名：")
    if username in userdatadict:
        userpwd = input("请输入您的密码：")
        if userpwd == userdatadict[username]:
            print("登录成功！")
            Game(username)
        else:
            while 1:
                userpwd = input("密码错误！请重新输入您的密码：")
                if userpwd == userdatadict[username]:
                    print("登录成功！")
                    Game(username)
    else:
        print("您的用户不存在，将自动前往注册")
        Signup_name()

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

def Game(username):
    print("#" * 50)
    print("欢迎来到Heros World！")
    worknum = input("请您选择您的职业：1:法师，2:战士     ")
    mage = ("法师",80,100,50)
    warrior = ("战士",100,50,100)
    if worknum == "1":
        work = mage[0]
        hp = mage[1]
        attack = mage[2]
        defense = mage[3]
        print("%s选择成功" % work)
    elif worknum == "2":
        work = warrior[0]
        hp = mage[1]
        attack = warrior[2]
        defense = warrior[3]
        print("%s选择成功" % work)
    else:
        work = mage[0]
        hp = mage[1]
        attack = mage[2]
        defense = mage[3]
        print("默认角色%s" % work)
    info = [username,work,hp,attack,defense]
    print("#" * 50)
    print("#    当前用户信息：                              #")
    print("#    用户名：%-10s血量：%6d              #" % (info[0],info[2]))
    print("#                      攻击力：%4d              #" % info[3])
    print("#    职业：%-10s防御力：%4d              #" % (info[1],info[4]))
    print("#" * 50)
    while 1:
        key = input("按m进入游戏地图：")
        if key == "m":
            Map()

def Map():
    worldmap = (['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'])
    x = 2
    y = 2
    while 1:
        if x == -5 or x == 5:
            x = 0
        if y == -5 or y == 5:
            y = 0
        worldmap[y][x] = "*"
        print("当前您身处位置：")
        print("-"*9)
        print("$","".join(worldmap[0]),"$")
        print("$","".join(worldmap[1]),"$")
        print("$","".join(worldmap[2]),"$")
        print("$","".join(worldmap[3]),"$")
        print("$","".join(worldmap[4]),"$")
        print("-"*9)
        move = input("请输入WASD移动（按q退出游戏）：")
        if move == "w":
            worldmap[y][x] = '#'
            y -= 1
        elif move == "s":
            worldmap[y][x] = '#'
            y += 1
        elif move == "d":
            worldmap[y][x] = '#'
            x += 1
        elif move == "a":
            worldmap[y][x] = '#'
            x -= 1
        elif move == "q":
            sys.exit(0)
        else:
            print("移动失败，请重新输入！")

Home()