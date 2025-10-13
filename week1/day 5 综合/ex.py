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

import re

def count_log_levels(log_file_path):
    """
    统计日志文件中各类型日志的数量
    
    Args:
        log_file_path: 日志文件路径
    
    Returns:
        dict: 包含各类型日志数量的字典
    """
    # TODO: 实现日志统计逻辑
    log_types = ['INFO','ERROR','WARNING', 'OK']
    log_counts = {k: 0 for k in log_types}
    pattern = re.compile(r'(?:[\[\(＜<【{]*\s*)\b(INFO|ERROR|WARNING|OK)\b(?:\s*[\]\)＞>】}]*\s*)',re.IGNORECASE)

    # [\[\(＜<]*  : []表示一个集合，*取一个或多个；  \[\(＜< 分别匹配[ ( ＜ <
    # \b(INFO|ERROR|WARNING|OK)\b:  \b \b 单词边界； (匹配集合)
    # (?:\(*\s*)     # 左侧若干个 "("，但不创建捕获组  ,搞不懂
    

    # log_counts = {
    #     'INFO': 0,
    #     'ERROR': 0,
    #     'WARNING': 0,
    #     'OK': 0
    # }
    
    # TODO: 读取文件并统计各类日志
    try:
        path = Path(log_file_path)
        if not path.is_file():
            raise FileNotFoundError(f"文件不存在: {log_file_path}")

        with path.open(encoding='utf-8') as f:
            for line in f:
                # 这写法又是什么。。
                if match := pattern.search(line):
                    level = match.group(1).upper()
                    log_counts[level] += 1
            # content = f.read()
            # log_counts['INFO'] = content.count('INFO')
            # log_counts['ERROR'] = content.count('ERROR')
            # log_counts['WARNING'] = content.count('WARNING')
            # log_counts['OK'] = content.count('OK')
    except Exception as e:
        print(f"文件异常 {e}")
        return None
    
    return log_counts

def write_result_to_json(result, output_file):
    """
    将结果写入JSON文件
    
    Args:
        result: 统计结果字典
        output_file: 输出文件路径
    """
    # TODO: 将结果写入JSON文件
    if result is None:
        print(f'没有内容写入， {result}')
        return 
    path = Path(output_file)
    with path.open('w',encoding="utf-8") as f:
        # f.write(json.dumps(result))
        json.dump(result, f, ensure_ascii=False, indent=4)
        
    print(f"结果已写入: {path.resolve()}")


def main():
    # TODO: 设置命令行参数解析
    parser = argparse.ArgumentParser(description="统计日志中 INFO/ERROR/WARNING/OK 的数量")
    parser.add_argument("--log", required=True, help="日志文件路径")
    parser.add_argument("--out", default="result.json", help="输出结果文件路径（默认 result.json）")

    args = parser.parse_args()
    
    write_file_name = args.out
    base_path = Path(__file__).parent
    output_file_path = base_path / write_file_name
    # TODO: 获取日志文件路径
    
    # TODO: 调用统计函数
    result = count_log_levels(base_path / args.log)
    # TODO: 写入结果到文件

   
    write_result_to_json(result, output_file_path)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"程序运行出错: {e}")

