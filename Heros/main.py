# Heros 2.0
# Creator: RealEcho
import sys
import random
import game

def Home():
    HomeInput = input("^欢迎来到Heros World！请选择：1.注册     2.登录（其他键退出）：").strip()
    if HomeInput == "1":
        Signup()
    elif HomeInput == "2":
        Login()
    else:
        sys.exit(0)

def Signup():
    print("#" * 50)
    print("欢迎来到Heros注册界面")
    UserDataFile = open("userdata.txt","a")
    UserDataFile.close()
    UserName = input("^请输入用户名（3 <= 用户名 < 9）：").strip()
    UserDataDict = File_Dict()
    if not UserName:
        UserName ='player' + str(random.randrange(101,199))
        print("检测到您未输入用户名，我们将随机生成一个您的用户名：",UserName)
    while UserName in UserDataDict:
        UserName = input("^您的用户名已存在，请重新输入您的用户名：").strip()
    while len(UserName) <= 3 or len(UserName) > 9:
        UserName = input("^您的用户名长度不符合规则，请重新输入您的用户名：").strip()
    UserPwd = input("^请输入密码（5 <= 密码 < 10）：").strip()
    while 5 >= len(UserPwd) or len(UserPwd) > 10:
        UserPwd = input("^您的密码长度不符合规则，请重新输入您的密码：").strip()
    SelectCareer = input("^请选择您的职业：1.战士     2.法师：").strip()
    Warrior = ("战士",120,80,100)
    Mage = ("法师",100,100,80)
    while 1:
        if SelectCareer == "1":
            SelectCareer = Warrior[0]
            UserHp = Warrior[1]
            UserAttack = Warrior[2]
            UserDefense = Warrior[3]
            break
        elif SelectCareer == "2":
            SelectCareer = Mage[0]
            UserHp = Mage[1]
            UserAttack = Mage[2]
            UserDefense = Mage[3]
            break
        else:
            SelectCareer = input("^请您重新选择职业：1.战士     2.法师：").strip()
    DefualtX = 5
    DefualtY = 2
    Dict_File(UserName,UserPwd,SelectCareer,UserHp,UserAttack,UserDefense,DefualtX,DefualtY)
    Login()

def Login():
    print("#" * 50)
    print("欢迎来到Heros登录界面")
    UserDataDict = File_Dict()
    UserName = input("^请输入您的用户名：").strip()
    if UserName in UserDataDict:
        UserPwd = input("^请输入您的密码：").strip()
        while 1:
            if UserPwd == UserDataDict[UserName][0]:
                UserDataList = [UserName,UserDataDict[UserName][1],int(UserDataDict[UserName][2]),int(UserDataDict[UserName][3]),int(UserDataDict[UserName][4]),int(UserDataDict[UserName][5]),int(UserDataDict[UserName][6])]
                game.UserInfo(UserDataList)
                break
            else:
                UserPwd = input("^密码错误！请重新输入您的密码：").strip()
    else:
        SelectNum = input("^您的用户名不存在！1.前往注册     2.退出游戏：").strip()
        while 1:
            if SelectNum == "1":
                Signup()
                break
            elif SelectNum == "2":
                sys.exit(0)
            else:
                SelectNum = input("^您的用户名不存在！1.前往注册     2.退出游戏：").strip()

def Dict_File(UserName,UserPwd,SelectCareer,UserHp,UserAttack,UserDefense,DefualtX,DefualtY):
    UserDataDict = {}
    UserDataDict[UserName] = [UserPwd,SelectCareer,UserHp,UserAttack,UserDefense,DefualtX,DefualtY]
    with open("userdata.txt","a") as UserDataFile:
        for UserName in UserDataDict:
            UserDataFile.write(str(UserName) + '-----' + str(UserPwd) + '-----' + str(SelectCareer) + '-----' + str(UserHp) + '-----' + str(UserAttack) + '-----' + str(UserDefense) + '-----' + str(DefualtX) + '-----' + str(DefualtY)  + '\n')

def File_Dict():
    UserDataDict = {}
    with open("userdata.txt","r") as UserDataFile:
        for line in UserDataFile.readlines():
            line = line.strip()
            UserName = line.split('-----')[0]
            UserPwd = line.split('-----')[1]
            SelectCareer = line.split('-----')[2]
            UserHp = line.split('-----')[3]
            UserAttack = line.split('-----')[4]
            UserDefense = line.split('-----')[5]
            DefualtX = line.split('-----')[6]
            DefualtY = line.split('-----')[7]
            UserDataDict[UserName] = UserPwd,SelectCareer,UserHp,UserAttack,UserDefense,DefualtX,DefualtY
        return UserDataDict

Home()