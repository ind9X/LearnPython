import math
import random
import sys

userdataname = ["admin","default"]
userdatapwd = ["123456","456789"]
name = "default"
pwd = "default"

def home():
    num = input("欢迎来到Heros World！请选择：1.注册     2.登录     ")
    if num == "1":
        signup_name()
    elif num == "2":
        login_name()
    else:
        print("选择有误！请重新选择。")
        home()

def signup_name():
    print("#" * 50)
    print("欢迎来到Heros World！注册界面")
    name = input("请输入您的用户名：")
    while len(name) != 0 and len(name) <= 3 or len(name) > 9:
        name = input("您的用户名长度不符合规则，请重新输入您的用户名：")
    while name in userdataname:
        name = input("用户名已存在！请重新输入：")
        while len(name) != 0 and len(name) <= 3 or len(name) > 9:
            name = input("您的用户名长度不符合规则，请重新输入您的用户名：")
    if not name:
        name = 'player' + str(random.randrange(101,199))
        print("检测到您未输入用户名，我们将随机生成一个您的用户名：",name)
        userdataname.append(name)
        signup_pwd()
    else:
        userdataname.append(name)
        signup_pwd()

def signup_pwd():
    pwd = input("请输入您的密码：")
    while 5 >= len(pwd) or len(pwd) > 10:
        pwd = input("您的密码长度不符合规则，请重新输入您的密码：")
    print("注册成功，请返回主页面登录！")
    userdatapwd.append(pwd)
    home()

def login_name():
    username = input("请输入您的用户名：")
    if username in userdataname:
        userindex = userdataname.index(str(username))
        login_pwd(userindex)
    else:
        print("您的用户不存在，将自动前往注册")
        signup_name()

def login_pwd(userindex):
    userpwd = input("请输入您的密码：")
    if userpwd == userdatapwd[userindex]:
        print("登录成功！")
        game(userindex)
    else:
        print("密码错误！")
        login_pwd(userindex)

def game(userindex):
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
    info = [userdataname[userindex],work,hp,attack,defense]
    print("#" * 50)
    print("#    当前用户信息：                              #")
    print("#    用户名：%-10s血量：%6d              #" % (info[0],info[2]))
    print("#                      攻击力：%4d              #" % info[3])
    print("#    职业：%-10s防御力：%4d              #" % (info[1],info[4]))
    print("#" * 50)
    map()

def map():
    worldMap = (['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'])
    row = 2
    col = 2
    while 1:
        if row == -5 or row == 5:
            row = 0
        if col == -5 or col == 5:
            col = 0
        worldMap[col][row] = "*"
        print("当前您身处位置：")
        print("-"*9)
        print("$","".join(worldMap[0]),"$")
        print("$","".join(worldMap[1]),"$")
        print("$","".join(worldMap[2]),"$")
        print("$","".join(worldMap[3]),"$")
        print("$","".join(worldMap[4]),"$")
        print("-"*9)
        move = input("请输入WASD移动（按q退出游戏）：")
        if move == "w":
            worldMap[col][row] = '#'
            col -= 1
        elif move == "s":
            worldMap[col][row] = '#'
            col += 1
        elif move == "d":
            worldMap[col][row] = '#'
            row += 1
        elif move == "a":
            worldMap[col][row] = '#'
            row -= 1
        elif move == "q":
            sys.exit(0)
        else:
            print("移动失败，请重新输入！")

home()