age = 18
if age >= 18:
    print("he is adult")
elif age >= 14:
    print("he is teenager")
else:
    print("he is child")

empty_list = []
# if 检测空列表时， 会认为其为False
if not empty_list:
    print("list is empty")
