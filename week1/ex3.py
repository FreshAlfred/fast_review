'''
用集合（set）实现两个测试集的去重与交集：

set1 = {"login", "logout", "payment", "search"}
set2 = {"search", "payment", "profile"}

输出：共同用例、仅在 set1 的用例、仅在 set2 的用例。
'''

set1 = {"login", "logout", "payment", "search"}
set2 = {"search", "payment", "profile"}

union_set = set1 | set2
print(union_set)
# 共同用例
common_set = set1 & set2
print(common_set)

# 仅在set 仅在set2
only_set1 = set1 - set2
print(only_set1)

only_set2 = set2 - set1
print(only_set2)

"""
对set的交并差操作不熟
你用 union_set - set2 得到仅在 set1 的用例，其实直接用 set1 - set2 更简洁；同理，仅在 set2 的用例可以用 set2 - set1。
另外，union_set 是并集，实际不需要用它来做差集。
"""