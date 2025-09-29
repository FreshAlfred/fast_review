# 写一个程序，找出 100–200 之间的所有质数。

from math import sqrt

result_list = []
for i in range(100, 201):
    for j in range(2, int(sqrt(i)) + 1):
        if(i % j == 0):
            break
    else:
        result_list.append(i)

print(result_list)

# 卧槽， 居然还有for-else 
# 它的作用是：只有当 for 循环没有被 break 终止时，才会执行 else 里的代码块。