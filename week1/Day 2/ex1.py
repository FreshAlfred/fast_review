'''
results = ["pass", "fail", "pass", "error", "pass", "fail"]
- 统计各结果数量
- 打印出第一个失败用例的位置
'''

# results = ["pass", "fail", "pass", "error", "pass", "fail"]
# dict = {}
# for i in results:
#     dict[i] = dict.get(i, 0) + 1


from collections import Counter

results = ["pass", "fail", "pass", "error", "pass", "fail"]
result_dict = Counter(results)
print(result_dict)
print(dict(result_dict))
# for i in results:
#     if i == 'fail':
#         print(results.index(i))
#         break;

'''
完全不知道 index是这么用的。。
'''
print(results.index('fail'))


'''
原理简述：
Counter 会遍历你传入的列表，每遇到一个元素就把它作为 key，出现一次就 value+1，和你用 dict.get(i, 0) + 1 的方式类似，但它已经帮你封装好了，代码更简洁。

优点：

代码简洁
提供了很多方便的方法（如 most_common()、直接加减 Counter 等）
本质上，Counter 就是一个自动计数的字典。

常用方法

from collections import Counter

results = ["pass", "fail", "pass", "error", "pass", "fail"]
counter = Counter(results)

# 1. most_common
print(counter.most_common(2))  # [('pass', 3), ('fail', 2)]

# 2. elements
print(list(counter.elements()))  # ['pass', 'pass', 'pass', 'fail', 'fail', 'error']

# 3. subtract
counter.subtract(['fail', 'error'])
print(counter)  # Counter({'pass': 3, 'fail': 1, 'error': 0})

# 4. update
counter.update(['pass', 'fail'])
print(counter)  # Counter({'pass': 4, 'fail': 2, 'error': 0})

# 5. total (Python 3.10+)
print(counter.total())  # 6
'''