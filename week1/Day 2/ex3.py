'''
使用 while 循环，模拟“重试机制”：
- 一个函数有 50% 概率失败
- 最多重试 3 次
- 如果仍失败，输出 "Test failed"
'''

# 完全没有思路啊。。。

import random

def flaky_func():
    return random.choice([True, False])

# attempt = 0
# success = False

# while attempt < 3:
#     attempt += 1
#     print(f"第{attempt}次尝试...")
#     if flaky_func():
#         print("success")
#         success = True
#         break

#     else:
#         print("Failed")


# if not success:
#    print("Test Failed")
# 改成for 循环

max_attempt = 3
for attempt in range(1, max_attempt + 1):
    print(f"第{attempt}次尝试...")
    if flaky_func():
        print("Success")
        break
    else:
        print("Failed")
else:
    print("Test Failed")