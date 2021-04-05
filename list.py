names = ['Mary', 'Jack', 'John']

print(names[0])
print(names[-1])

names.append("Jerry")
print(names)

names.insert(1, "Max")
print(names)

del names[2]
print(names)

name = names.pop()
print(f"{names} pop {name}")

name = names.pop(0)
print(f"{names} pop 0 : {name}")

names.append("Anna")
names.append("Anna")
# remove 只移除找到的第一个匹配值
names.remove("Anna")
print(names)

# 有副作用
names.sort()
print(names)

# 无副作用
names_sorted = sorted(names, reverse=True)
print(names_sorted)

# 反转顺序， 有副作用
names.reverse()
print(names)

print(f"The size of names is {len(names)}")
