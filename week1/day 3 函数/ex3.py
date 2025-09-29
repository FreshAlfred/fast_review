# 写一个函数 `fibonacci(n)`，返回前 n 个斐波那契数（用循环实现）。

# def fibonacci(n):
    
#     if not n:
#         raise ValueError("请输入有效整数")
#     if type(n) != type(1):
#         raise ValueError("请输入有效整数")
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1, 1]
#     if n > 2:
#         result_list = [1, 1]
#         for i in range(2, n):
#             temp = result_list[i-1] + result_list[i-2]
#             result_list.append(temp)
#         return result_list
        
# print(fibonacci(4))


def fibonacci(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("请输入正整数")
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    result_list = [1, 1]
    for i in range(2, n):
        temp = result_list[i-1] + result_list[i-2]
        result_list.append(temp)
    return result_list

'''
 isinstance(n, int) 替代 type(n) != type(1)
 建议判断 n 是否为正整数（n > 0），否则 n=0 或负数时会出错。
'''