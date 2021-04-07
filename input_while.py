height = input('How tall are you? ')
height = int(height)
if height > 170:
    print("You are taller")
else:
    print("You are short")

pets = ['cat', 'monkey', 'chicken', 'dog', 'cat']
i = 0
# 利用while 移除某个指定元素
while 'cat' in pets:
    pets.remove('cat')
    i = i + 1
    print(f'loop {i}')
