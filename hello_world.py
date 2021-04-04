message = "hello world"
print(message)

# 将单词转换成首字母大写
print(message.title())
print("WE ARE THE ONLY ONE!".title())

# 3.6 以及之后的版本才有
print(f"show: {message}")

# trim
a_str = " python "
print(a_str.strip())
print(a_str.rstrip())
print(a_str.lstrip())

# float, 对于除法计算，无论是否整除，结果都是浮点数
print(4 / 2)
