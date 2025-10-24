#列表（list）是一种可变序列类型，我们可以追加、插入、删除和替换列表中的元素
list1 = list("Hello,This is a list.")
print(list1)  # 输出列表的所有元素

list2 = [1, 2, 3, 4, 5]
print(list2)  # 输出列表的所有元素

#给list1列表对象追加多个元素
list1.extend(['New', 'Elements'])
print(list1)  # 输出更新后的列表

#给list2列表对象追加单个元素
list2.append(6)
print(list2)  # 输出更新后的列表

#往队列中插入一个元素
list2.insert(4,7)
print(list2)  # 输出更新后的列表

#替换列表中的某个元素
list2[0] = 10
print(list2)  # 输出更新后的列表

#移除列表中的元素
list2.remove(3)
print(list2)  # 输出更新后的列表

