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