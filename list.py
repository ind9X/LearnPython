"""
a = input("请输入：")
b = []
while a != "q":
    b.append(a)
    a = input("请输入：")
print(b)


x = ["1","2","3","4","5"]
x.reverse()
print(x)
"""
import sys
team1txt = input("请输入第一支队伍：")
team2txt = input("请输入第二支队伍：")
team1 = []
team2 = []
def team_score():
    team = input("请选择给哪支队伍进行加分：1.%s     2.%s     （输入g出结果，输入q退出）" % (team1txt,team2txt))
    while team == "1":
        score = input("请输入%s得分（输入q返回上一层）："% team1txt)
        if score == "q":
            team_score()
        else:
            try:
                score = int(score)
            except ValueError:
                print("输入错误，请重新输入！")
            else:
                score = int(score)
                team1.append(score)
    while team == "2":
        score = input("请输入%s得分（输入q返回上一层）：" % team2txt)
        if score == "q":
            team_score()
        else:
            try:
                score = int(score)
            except ValueError:
                print("输入错误，请重新输入！")
            else:
                score = int(score)
                team2.append(score)
    if team == "g":
        print("%s得分：" % team1txt,sum(team1))
        print("%s得分：" % team2txt,sum(team2))
        if sum(team1) > sum(team2):
            print("Winner is %s!" % team1txt)
        elif sum(team1) < sum(team2):
            print("Winner is %s!" % team2txt)
        else:
            print("Draw!")
        sys.exit(0)
    elif team == "q":
        sys.exit(0)
    else:
        print("输入的选项有误，请重新选择！")
        team_score()
team_score()