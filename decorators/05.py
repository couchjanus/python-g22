class DecoratorTest(object):
    def __init__(self):
        """Конструктор"""
        pass

    # обычный метод
    def doubler(self, x):
        print("умножаем на 2")
        return x*2

    @classmethod
    def class_tripler(сls, x):
        print("умножаем на 3: %s" % сls)
        return x*3

    @staticmethod
    def static_quad(x):
        print("умножаем на 4")
        return x*4

if __name__ == "__main__":
    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))
    print(DecoratorTest.class_tripler(3))
    print(DecoratorTest.static_quad(2))
    print(decor.static_quad(3))


# Этот пример демонстрирует, что вы можете вызывать обычный метод и оба метода декоратора одним и тем же путем. Обратите внимание на то, что вы можете вызывать обе функции @classmethod и @staticmethod прямо из класса или из экземпляра класса. Если вы попытаетесь вызвать обычную функцию при помощи класса (другими словами, DecoratorTest.doubler(2)), вы получите ошибку TypeError. Также стоит обратить внимание на то, что последний оператор вывода показывает, что decor.static_quad возвращает обычную функцию вместо связанного метода.
