def secondFunction(a,b):
    c = input("请输入一个数字:")
    print("您输入的数字是:",c)
    print("交换前:a =",a," b =",b)
    c = a^b
    a = a^c
    b = a^c
    print("交换后:a =",a," b =",b)
    return a,b
#-------------测试secondFunction函数---------------
# x = 10
# y = 20
# x,y = secondFunction(x,y)
# print("函数调用后:x =",x," y =",y)
