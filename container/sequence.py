#序列（sequence）是一种可迭代的、元素有序的容器类型的数据
#序列包括列表（list）、字符串（str）、元组（tuple）和字节序列（bytes）等。

#索引
hello = 'Hello'
print(hello[0])      # 输出 'H'
print(hello[0:5])   # 输出 'World'
print(hello[-1])     # 输出 'o'
#hello[13]    # 抛出 IndexError 异常，因为索引超出范围

#max&&min&&len
final = max(hello)
first = min(hello)
len_hello = len(hello)
print(final)      # 输出 'o'
print(first)      # 输出 'H'
print(len_hello)  # 输出 5

#拼接、重复和切片
hello = 'hello'
world = 'world'
helloworld = hello + ' ' + world
print(helloworld)  # 输出 'hello world'

repeat_hello = hello * 3
print(repeat_hello)  # 输出 'hellohellohello'

hl = hello[0:3:2]
print(hl)  # 输出 'hl'

#成员测试
print('e' in hello)    # 输出 True
print('a' not in hello) # 输出 True

E = 'E'
bool = E in hello
print(bool)  # 输出 False
