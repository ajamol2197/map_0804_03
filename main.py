# 1
roy = [2, 4, 6, 8]
print(roy)

a = list(map(lambda d: d + 1, roy))
print(a)

# 2
roy = ["a", "b", "c"]
print(roy)

aa = list(map(lambda d: d * 3, roy))
print(aa)

# 3
roy = [7, 14, 21]
print(roy)

a = list(map(lambda d: d / 7, roy))
print(a)

# 4
roy = ["Python", "Java", "C++"]
print(roy)

a = list(map(lambda d: d.lower(), roy))
print(a)

# 5
roy = [1, 2, 3, 4]
print(roy)

a = list(map(lambda d: f"son: {d}", roy))
print(a)

# 6
roy = ["10", "20", "30"]
print(roy)

a = list(map(lambda d: int(d) + 10, roy))
print(a)

# 7
roy = [9, 16, 25]
print(roy)

a = list(map(lambda d: d ** 0.5, roy))
print(a)

# 8
roy = ["olma", "anor", "uzum"]
print(roy)

a = list(map(lambda d: d[0], roy))
print(a)

# 9
roy = [11, 22, 33, 44]
print(roy)

a = list(map(lambda d: str(d), roy))
print(a)

# 10
roy = ["python", "map", "function"]
print(roy)

a = list(map(lambda d: len(d) * 2, roy))
print(a)
