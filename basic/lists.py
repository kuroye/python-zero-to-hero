my_list = [10, '20', 'June', True]

for i, element in enumerate(my_list):   # 将可遍历对象分解为index和单独对象
    my_list[i] = str(element)

print(' '.join(my_list))

# print(' '.join(                               进阶写法
#     [str(element) for element in my_list]
# ))
