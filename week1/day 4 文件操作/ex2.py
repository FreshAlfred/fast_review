# 读取一个 JSON 文件并统计字段数量。
'''
自己的思路， json转换成dict，然后直接用size?
'''

# from pathlib import Path
# import json

# base_path = Path(__file__).parent
# json_path = base_path / 'test.json'

# try:
#     with open(json_path, 'r', encoding='utf-8') as f:
#         a_dict = json.load(f)
#     print(len(a_dict))
# except FileNotFoundError:
#     print("未找到文件")
# except json.JSONDecodeError:
#     print("JSON 格式错误")
# except Exception as e:
#     print("未知错误")


'''
load和loads的区别：
load 处理文件对象
loads 处理字符串


with 语句会自动调用对象的 __enter__ 和 __exit__ 方法。
进入 with 块时运行 __enter__，离开时（无论是否异常）运行 __exit__，实现资源的自动管理和释放。
'''

'''
from pathlib import Path

# 获取当前目录
# os.path.dirname(__file__)  ->  Path(__file__).parent

# 路径拼接
# os.path.join(base_path, "test.json")  ->  base_path / "test.json"

# 检查文件是否存在
# os.path.exists(path)  ->  path.exists()

# 获取文件名
# os.path.basename(path)  ->  path.name

# 获取文件扩展名
# os.path.splitext(path)[1]  ->  path.suffix

'''

'''
考虑嵌套和异常
'''

import json
from pathlib import Path

base_path = Path(__file__).parent
json_path = base_path / 'list.json'

def count_fields(obj):
    if isinstance(obj, dict):
        return len(obj) + sum(count_fields(v) for v in obj.values())
    elif isinstance(obj, list):
        return sum(count_fields(item) for item in obj)
    return 0

def load_json(file_path):
    try:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")
        with path.open(encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"JSON 格式错误: {e}")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None

data = load_json(json_path)
if data:
    print(f"总字段数量: {count_fields(data)}")


'''
明天自己写一遍！！
'''

