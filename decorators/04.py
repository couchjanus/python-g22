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

if __name__ == "__main__":
    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))
    print(DecoratorTest.class_tripler(3))
