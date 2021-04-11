# 使用with, python 会自动关闭它

filename = "./input/some.txt"
with open(filename) as file:
    content = file.read()
    print(content)

with open(filename) as file:
    content_list = file.readlines()

print(content_list)

o_filename = "./tmp/out.txt"
# 如果文件存在 python 会先清空它
with open(o_filename, 'w') as file:
    file.write("hello world\n")
# 附件模式会在末尾插入文本
with open(o_filename, 'a')as file:
    file.write("I am a programmer.\n")



