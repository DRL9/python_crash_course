names = ['Mark', 'Mary', 'Claud', 'Jim', 'Hary']
for name in names:
    print(name)

for num in range(1, 5):
    print(f"num is {num}")

print(range(1, 5))
numbers = list(range(1, 5))
print(numbers)
print(reversed(numbers))
# list() 可以将 可迭代对象转换成 list
print(list(reversed(numbers)))

print(min(numbers), sum(numbers), max(numbers))

# 列表解析
squares = [value ** 3 for value in range(1, 11)]
print(f"squares is {squares}")

# 切片生成新的list
sub_squares = squares[1:3]
sub_squares[0] = 10
print(f"square: {squares}, sub: {sub_squares}")

# 复制列表
copy_list = squares[:]
print(f"copy {copy_list}")

# 元组， 不可变的数据
dim = (10, 20)
print(f"dim is {dim}")
