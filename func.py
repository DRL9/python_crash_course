# 导入模块
import module_1
from module_1 import say_hi
import module_1 as m1
from module_1 import greeting_one as greet
from module_1 import *


# 默认值必须要后面
def greeting(name, gender, age=0):
    print(f"I'm {name.title()}, my gender is {gender}, age is {age}")


# 位置实参
greeting('John', 'male')

# 关键字实参
greeting(name="Mary", gender="female")

greeting("Jerry", "female")


def sum_numbers(*nums):
    """
    *nums 接受不定个参数， 其中nums 是元组
    :param nums: {int}
    :return: {int}
    """
    total = 0
    for num in nums:
        total += num
    return total


print(f"sum is {sum_numbers(1, 2, 3, 6)}")


def build_profile(**info):
    """
    **info 表示任意数量的关键字形参, info 是 map
    :param info:
    :return:
    """
    print(f"first is {info.get('first', '')}, last is {info.get('last', '')}")
    return info


build_profile(first='Mary', last="Holy")

module_1.say_hi()
module_1.greeting_one()

say_hi()
