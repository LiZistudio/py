#序列（sequence）是一种可迭代的、元素有序的容器类型的数据
#序列包括列表（list）、字符串（str）、元组（tuple）和字节序列（bytes）等。
hello = "Hello"
print(hello[0])      # 输出 'H'
print(hello[0:5])   # 输出 'World'
print(hello[-1])     # 输出 'o'
#hello[13]    # 抛出 IndexError 异常，因为索引超出范围

final = max(hello)
first = min(hello)
len_hello = len(hello)
print(final)      # 输出 'o'
print(first)      # 输出 'H'
print(len_hello)  # 输出 5
