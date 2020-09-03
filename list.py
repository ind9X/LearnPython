"""
a = input("请输入：")
b = []
while a != "q":
    b.append(a)
    a = input("请输入：")
print(b)
"""
"""
x = ["1","2","3","4","5"]
x.reverse()
print(x)
"""
rockets = []
lakers = []
def team_score():
    team = input("请输入队伍名称：1.火箭     2.湖人     （输入“g”出结果）")
    while team == "1":
        score = input("请输入火箭队得分（输入q返回上一层）：")
        if score == "q":
            team_score()
        else:
            score = int(score)
            rockets.append(score)
    while team == "2":
        score = input("请输入湖人队得分（输入q返回上一层）：")
        if score == "q":
            team_score()
        else:
            score = int(score)
            lakers.append(score)
    while team == "g":
        print("火箭队得分：",sum(rockets))
        print("湖人队得分：",sum(lakers))
        if sum(rockets) > sum(lakers):
            print("Winner is Rockets!")
        elif sum(rockets) < sum(lakers):
            print("Winner is Lakers!")
        else:
            print("Draw!")
    print("输入的选项有误，请重新选择！")
    team_score()
team_score()