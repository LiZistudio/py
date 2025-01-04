# coding=utf-8

import world
from world import z
from world import x as x2


str = "开门见山"
print(str)
x = 100
y = 20
w = -10

print(y)        # 20
print(world.y)  # True
print(z)        # 20.0
print(x2)       # 你好
print(w)


score = int(input("请输入您的分数:"))
if (score < 0) or (score > 100) :
    print("输入有误，请重新输入。")
elif score > 80 :
    print("优秀")
elif score > 60 :
    print("及格")
else :
    print("加油")


#-------------while循环计算水仙花数---------------
print("while循环计算水仙花数")
i = 100; u = 0; v = 0; w = 0

while i < 1000 :
    u = i // 100
    v = (i-u*100)//10
    w = i-u*100-v*10
    if i == (u**3+v**3+w**3) :
        print("i = ",i)
    i += 1
else :
    print("循环结束")

#--------------for循环计算水仙花数----------------
print("for循环计算水仙花数")
u = 0; v = 0; w = 0
for i in range(100,1000):
    u = i // 100
    v = (i-u*100)//10
    w = i-u*100-v*10
    if i == (u**3+v**3+w**3) :
        print("i = ",i)
else :
    print("循环结束")
