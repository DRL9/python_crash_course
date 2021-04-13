import unittest
from func import sum_numbers
from class_ex import Car


# 继承自 TestCase
class FuncTestCase(unittest.TestCase):
    # 每个用例都会现运行这个
    def setUp(self):
        print("test start")
        self.car = Car(make="bmw", model="a1", year=1990)

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(1, 2, 3), 6)

    def test_get_descriptive_name(self):
        self.assertEqual(self.car.get_descriptive_name(), "1990 Bmw A1")

    def test_make(self):
        self.assertIn(self.car.make, ['bmw'])


if __name__ == '__main__':
    unittest.main()
