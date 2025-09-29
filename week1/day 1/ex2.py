'''
2、 给定字符串：
    ”error:404，ok:200，fail:500，ok:200"
    期望输出:
    {'error':1，'ok':2，'fail':1}
'''

s = "error:404,ok:200,fail:500，ok:200"
# 替换中文逗号为英文逗号，多加一步，兼容性更好
s = s.replace("，", ",")

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

PS：
CMD命令
& D:/_env/python311/python.exe .\week1\ex2.py
指定某个执行器运行 可执行程序
'''


