import math
import random
def Game():
    print("#" * 50)
    name = input("请输入您的用户名：")
    pwd = input("请输入您的密码：")
    hp = 100
    if not name:
        name = 'player' + str(random.randrange(101,199))
    if len(pwd) < 6:
        while 1:
            pwd = str(input("请重新输入您的密码："))
            if len(pwd) >= 6:
                break
    worknum = input("请您选择您的职业：1:法师，2:战士     ")
    mage = ("法师",100,50)
    warrior = ("战士",50,100)
    if worknum == "1":
        work = mage[0]
        attack = mage[1]
        defense = mage[2]
        print("%s选择成功" % work)
    elif worknum == "2":
        work = warrior[0]
        attack = warrior[1]
        defense = warrior[2]
        print("%s选择成功" % work)
    else:
        work = mage[0]
        attack = mage[1]
        defense = mage[2]
        print("默认角色%s" % work)
    info = [name,work,hp,attack,defense]
    print("#" * 50)
    print("#    当前用户信息：                              #")
    print("#    用户名：%-10s血量：%6d              #" % (info[0],info[2]))
    print("#                      攻击力：%4d              #" % info[3])
    print("#    职业：%-10s防御力：%4d              #" % (info[1],info[4]))
    print("#" * 50)
Game()