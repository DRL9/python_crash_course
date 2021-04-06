alien = {"y_pos": 1, "x_pos": 2}
print(alien)
# 3.7之后，元素的排列顺序与添加时一致
for i in alien:
    print(i)

del alien['x_pos']
print(alien)
# 如果使用alien['x_pos'] 会抛出异常
print(alien.get("x_pos"))
alien['z_pos'] = 11

for key, value in alien.items():
    print(f"{key}: {value}")
# 与 for key in alien: 结果一致
for key in alien.keys():
    print(f"key: {key}")

for val in alien.values():
    print(f"val: {val}")
