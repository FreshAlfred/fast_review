'''
编写一个脚本，实现：

统计各类型日志数量（INFO, ERROR, WARNING, OK）

将结果写入 result.json 文件

进阶挑战：

增加参数，让用户指定日志文件路径。

捕获文件不存在异常。

'''
import json
import argparse
from pathlib import Path

def count_log_levels(log_file_path):
    """
    统计日志文件中各类型日志的数量
    
    Args:
        log_file_path: 日志文件路径
    
    Returns:
        dict: 包含各类型日志数量的字典
    """
    # TODO: 实现日志统计逻辑
    log_counts = {
        'INFO': 0,
        'ERROR': 0,
        'WARNING': 0,
        'OK': 0
    }
    
    # TODO: 读取文件并统计各类日志

    
    return log_counts

def write_result_to_json(result, output_file):
    """
    将结果写入JSON文件
    
    Args:
        result: 统计结果字典
        output_file: 输出文件路径
    """
    # TODO: 将结果写入JSON文件


def main():
    # TODO: 设置命令行参数解析

    
    # TODO: 获取日志文件路径
    
    # TODO: 调用统计函数
    
    # TODO: 写入结果到文件
    
    pass

if __name__ == "__main__":
    main()