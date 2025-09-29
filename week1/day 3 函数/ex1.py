# 写一个函数 `calc_stats(*scores)`，返回：平均值、最大值、最小值。

def calc_stats(*scores):
    if not scores:
        raise ValueError("请输入至少一个数")
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    return max_score, min_score, avg_score

print(calc_stats(11,22,33))
# print(calc_stats())


