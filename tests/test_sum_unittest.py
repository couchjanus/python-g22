# Импортировать unittest из стандартной библиотеки;
import unittest

# test case - минимальный блок тестирования. Проверяет ответы для разных наборов данных.
# в качестве первого аргумента функция sum() в Python принимает любой итерируемый объект.

# Создать класс, который будет наследовать класс TestCase;
class TestSum(unittest.TestCase):

    # Создать методы, использовать self.assertEqual() метод
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()



