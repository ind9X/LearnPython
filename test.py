import math
import random
def Game():
    print("###################################################")
    name = input("请输入您的用户名：")
    pwd = input("请输入您的密码：")
    hp = 100
    attack = 100
    defense = 50
    if not name:
        name = 'player' + str(random.randrange(101,199))
    if len(pwd) < 6:
        while 1:
            pwd = str(input("请重新输入您的密码："))
            if len(pwd) >= 6:
                break
    work = input("请您选择您的职业：1:法师，2:战士     ")
    if work == "1":
        work = "法师"
        print(work,"选择成功")
    if work == "2":
        work = "战士"
        print(work,"选择成功")
    if not work:
        work = "法师"
        print("默认角色",work)
    userdata = [name,work,hp,attack,defense]
    print("###################################################")
    print("当前用户信息：")
    print("用户名：",userdata[0],"职业：",userdata[1],"HP：",userdata[2],"攻击力：",userdata[3],"防御力：",userdata[4])
Game()