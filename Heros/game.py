import sys

def Game(UserDataList):
    WorldMap = (['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'])
    x = UserDataList[5]
    y = UserDataList[6]
    while 1:
        if x == -5 or x == 5:
            x = 0
        if y == -5 or y == 5:
            y = 0
        WorldMap[y][x] = "*"
        print("当前您身处位置：")
        print("-"*9)
        print("$","".join(WorldMap[0]),"$")
        print("$","".join(WorldMap[1]),"$")
        print("$","".join(WorldMap[2]),"$")
        print("$","".join(WorldMap[3]),"$")
        print("$","".join(WorldMap[4]),"$")
        print("-"*9)
        Move = input("请输入WASD移动（q退出，p显示当前角色信息）：")
        if Move == "w":
            WorldMap[y][x] = '#'
            y -= 1
        elif Move == "s":
            WorldMap[y][x] = '#'
            y += 1
        elif Move == "d":
            WorldMap[y][x] = '#'
            x += 1
        elif Move == "a":
            WorldMap[y][x] = '#'
            x -= 1
        elif Move == "q":
            sys.exit(0)
        elif Move == "p":
            UserInfo(UserDataList)
        else:
            print("移动失败，请重新输入！")

def UserInfo(UserDataList):
    print("#" * 50)
    print("当前用户信息：")
    print("用户名：%-16s职业：%-10s\n血量：%-5s攻击力：%-5s防御力：%-5s" % (UserDataList[0],UserDataList[1],UserDataList[2],UserDataList[3],UserDataList[4]))
    print("#" * 50)
    while 1:
        key = input("按m进入游戏（其他键退出）：")
        if key == "m":
            Game(UserDataList)
        else:
            sys.exit(0)