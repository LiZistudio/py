#元组是一种不可变序列类型
tuple1 = (1,2)
print(tuple1)  # 输出 (1, 2)
tuple2 = tuple(['a', 'b', 'c'])
print(tuple2)  # 输出 ('a', 'b', 'c')

first = tuple1[1]
print(first)  # 输出 2

#拆包
a, b = tuple1
print(a)  # 输出 1
print(b)  # 输出 2
