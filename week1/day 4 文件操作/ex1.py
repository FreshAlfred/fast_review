# 写一个脚本，读取日志文件 `test.log`，提取所有包含 `"ERROR"` 的行，并写入到 `error.log`。

with open('test.log') as s:
    a = s.readline()
    