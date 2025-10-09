# 写一个脚本，读取日志文件 `test.log`，提取所有包含 `"ERROR"` 的行，并写入到 `error.log`。

import os

base_path = os.path.dirname(__file__)
test_log = os.path.join(base_path, 'test.log')
error_log = os.path.join(base_path, 'error.log')

with open(test_log) as s, open(error_log, 'w') as f:
	for line in s:
		if "ERROR" in line:
			f.write(line)




'''
加入base路径保证随时能用；

常见写入模式：
'w'：写入模式，覆盖原有内容。如果文件不存在则新建。
'a'：追加模式，写入内容追加到文件末尾。如果文件不存在则新建。
'x'：独占写入模式，文件不存在时新建，存在则报错。
'wb'、'ab'：以二进制方式写入或追加。


__file__ 是 Python 的内置变量，表示当前脚本文件的路径（字符串类型）。

'''