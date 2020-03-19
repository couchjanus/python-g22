# Можно ли суммировать список целых чисел?
# Можно ли суммировать кортеж или множество?
# Можно ли суммировать список чисел с плавающей точкой?
# Что будет, если дать на вход плохое значение: одно целое число или строку?
# Что будет, если одно из значений отрицательное?

# Импортировать unittest из стандартной библиотеки;
import unittest
# импорт типа Fraction из модуля fractions стандартной библиотеки.
from fractions import Fraction

from my_sum import sum
from my_sum import __version__
import sys

# Определяет новый класс тест-кейса под названием TestSum, наследующий unittest.TestCase;
class TestSum(unittest.TestCase):
    # Определяет тестовый метод .test_list_int() для тестирования целочисленного списка. 
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    # sum() должен принимать на вход другие списки числового типа, например дроби.
    # добавим тест с утверждением, ожидая некорректное значение. 
    # ожидаем, что сумма ¼, ¼ и ⅖ будет равна 1:

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)
    
    # Этот тест-кейс будет пройден, только если sum(data) выдаст TypeError. 
    # Вы можете заменить TypeError на любой другой тип исключений.

    def test_bad_type(self):
        data = "bla bla bla"
        with self.assertRaises(TypeError):
            result = sum(data)

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(__version__ < '1', "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

if __name__ == '__main__':
    unittest.main()
