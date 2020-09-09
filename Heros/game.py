import sys
import random

def Game(UserDataList):
    WorldMap = (['#','#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#','#'],['#','#','#','#','#','#','#','#','#','#','#'])
    x = UserDataList[5]
    y = UserDataList[6]
    AppleMove = Apple(WorldMap)
    MonsterMove = Monster(WorldMap)
    while 1:
        if x == -11 or x == 11:
            x = 0
        if y == -5 or y == 5:
            y = 0
        WorldMap[y][x] = "*"
        print("当前您身处位置：")
        print("-"*15)
        print("$","".join(WorldMap[0]),"$")
        print("$","".join(WorldMap[1]),"$")
        print("$","".join(WorldMap[2]),"$")
        print("$","".join(WorldMap[3]),"$")
        print("$","".join(WorldMap[4]),"$")
        print("-"*15)
        MoveInput = input("^请输入WASD移动（q退出，p显示当前角色信息）：")
        MoveList = Move(UserDataList,MoveInput,WorldMap,x,y)
        x = MoveList[0]
        y = MoveList[1]
        AppleX = AppleMove[0]
        AppleY = AppleMove[1]
        MonsterX = MonsterMove[0]
        MonsterY = MonsterMove[1]
        if x == AppleX and y == AppleY:
            UserDataList[2] += 20
            print("您吃了一个苹果，HP加20")
        elif x == MonsterX and y == MonsterY:
            UserDataList[2] -= 40
            print("您与怪物战斗，HP减40")

def UserInfo(UserDataList):
    print("#" * 50)
    print("当前用户信息：")
    print("用户名：%-16s职业：%-10s\n血量：%-5s攻击力：%-5s防御力：%-5s" % (UserDataList[0],UserDataList[1],UserDataList[2],UserDataList[3],UserDataList[4]))
    print("#" * 50)
    while 1:
        key = input("^按m进入游戏（其他键退出）：")
        if key == "m":
            Game(UserDataList)
        else:
            sys.exit(0)

def Move(UserDataList,MoveInput,WorldMap,x,y):
    if MoveInput == "w":
        WorldMap[y][x] = '#'
        y -= 1
    elif MoveInput == "s":
        WorldMap[y][x] = '#'
        y += 1
    elif MoveInput == "d":
        WorldMap[y][x] = '#'
        x += 1
    elif MoveInput == "a":
        WorldMap[y][x] = '#'
        x -= 1
    elif MoveInput == "q":
        sys.exit(0)
    elif MoveInput == "p":
        UserInfo(UserDataList)
        sys.exit(0)
    else:
        print("移动失败，请重新输入！")
    return [x,y]

def Apple(WorldMap):
    AppleX = random.randrange(11)
    AppleY = random.randrange(5)
    WorldMap[AppleY][AppleX] = "@"
    return AppleX,AppleY

def Monster(WorldMap):
    MonsterX = random.randrange(11)
    MonsterY = random.randrange(5)
    WorldMap[MonsterY][MonsterX] = "&"
    return MonsterX,MonsterY