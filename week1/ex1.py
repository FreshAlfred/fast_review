'''
写一个程序:
    接收用户输入的测试用例执行时间(秒)，存入列表;
    输出:
        平均执行时间
        最快和最慢用例
'''
list = []

# def get_time():
#     time = input('请输入测试用例执行时间(秒):')
#     list.append(float(time))

# def test_report(list):
#     avg_time = sum(list)/len(list)
#     print('平均执行时间:',avg_time)
#     print('最快用例:',min(list))
#     print('最慢用例:',max(list))

# while True:
#     get_time()
#     flag = input('是否继续输入(y/n):')
#     if flag == 'n':
#         break

# test_report(list)

'''
您的代码已经实现了基本功能，可以进一步优化：

1、避免使用 list 作为变量名，因为它是 Python 的内置类型名。
2、输入校验，防止用户输入非数字或负数。
3、将输入和报告逻辑封装到主函数，提高可读性。
4、使用列表推导式或循环收集数据，更简洁。
'''

def get_time():
    times = []
    while True:
        try:
            time = float(input('请输入测试用例执行时间(秒):'))
            if time < 0:
                print('请输入非负数')
                continue
            times.append(time)
        except ValueError:
            print('请输入有效数字')
            continue
        flag =  input('是否继续输入(y/n):')
        if flag.lower() == 'n':
            break
    return times

def test_report(times):
    if not times:
        print('没有输入任何数据。')
        return
    avg_time = sum(times) / len(times)
    print('平均执行时间:', avg_time)
    print('最快用例:', min(times))
    print('最慢用例:', max(times))

def main():
    times = get_time()
    test_report(times)

if __name__ == '__main__':
    main()

# 试试