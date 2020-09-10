"""
class Ren():
    name = 'body'
    def say(self):
        print("i am %s" % self.name)
zhang = Ren()
li = Ren()
li.name = 'lisi'
print(zhang.name)
zhang.name = "zhangsan"
print(zhang.name)
print(li.name)
zhang.say()
"""
"""
class HomeWork:
    Name = ''
    Age = 0
    __Qq = ''
    def __init__(self,n,a,q):
        self.Name = n
        self.Age = a
        self.__Qq = q
    def Speak(self):
        print("%s说：我%d岁，我的QQ号是：%s" % (self.Name,self.Age,self.__Qq))
p = HomeWork('RealEcho',21,'10001')
p.Speak()
"""
"""
class Body():
    name = ''
    __money = 0
    def __init__(self,name = ''):
        self.name = name
    def Say(self,msg):
        print(msg)
        print(self.name)
        print(self.__money)

class Man(Body):
    def Say(self):
        print("Mannnnnnnnnnnnnnnnnnnnn")
    def Drive(self):
        print("Doooooooooooooooooooooo")

zhang = Man()
print(zhang.name)
zhang.Say()
zhang.Drive()
"""
"""
class hero():
    def __init__(self, name = '', hp = 0, hit = 0):
        self.name = name
        self.hp = hp
        self.hit = hit
        print("角色姓名：",name,"血量：",hp,"攻击力：",hit)
    
    def act(self,other):
        return other.hp - self.hit

if __name__ == '__main__':
    zhang = hero('ZhangSan',100,50)
    lisi = hero('LiSi',80,70)
    print(zhang.act(lisi))
"""
class hero():
    def __init__(self, name, hp, hit):
        self.name = name
        self.hp = hp
        self.hit = hit
        print(name, hp, hit)
    def attack(self, other):
        final = other.hp - self.hit
        print(self.name, "剩余：", final, "的血量")

ind9X = hero('ind9X', 100, 60)
RealEcho = hero('RealEcho', 80, 70)
ind9X.attack(RealEcho)