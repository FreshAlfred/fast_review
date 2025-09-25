'''
2、 给定字符串：
    ”error:404，ok:200，fail:500，ok:200"
    期望输出:
    {'error':1，'ok':2，'fail':1}
'''

s = "error:404,ok:200,fail:500,ok:200"
result = {}
for item in s.split(','):
    key = item.split(':')[0]
    result[key] = result.get(key, 0) + 1

print(result)

'''
未掌握
dict.get(key, 0)的用法；

dict.get(key)：如果字典中有这个键，返回对应的值；如果没有，返回 None。
dict.get(key, 0)：如果字典中有这个键，返回对应的值；如果没有，返回 0（你可以把 0 换成任何你想要的默认值）。
dict[key]：如果字典中没有这个键，会直接抛出 KeyError 异常。

'''