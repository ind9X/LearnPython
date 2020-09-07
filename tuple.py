#20200907
"""
thistuple = ("apple","banana","cherry","orange","mango")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:4])

t1 = ("apple")
t2 = ("apple",)
print(type(t1))
print(type(t2))

x = ("apple","banana","cherry")
y = list(x)
y[1] = "mango"
x = tuple(y)
print(x)

a = ("apple",)
print(a)
del a
#print(a)

tuple1 = ("apple",)
tuple2 = (1,)
tuple3 = tuple1 + tuple2
print(tuple3).
"""

a = (i for i in range(1,1000) if i % 3 == 0 and i % 5 == 0)
print(sum(a))