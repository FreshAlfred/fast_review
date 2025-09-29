# 写一个函数 merge_results(**kwargs)，可以接收多个命名参数，比如：
# merge_results(pass_count=30, fail_count=5, error_count=2)
# 输出一个字典：{'pass_count': 30, 'fail_count': 5, 'error_count': 2}


def merge_results(**kwargs):
    # result_dict = {}
    # for k, v in kwargs.items():
    #     result_dict[k] = v
    # return result_dict
    return kwargs
print(merge_results(pass_count=30, fail_count=5, error_count=2))

'''
字典赋值是 dick[key] 中括号！！！
'''