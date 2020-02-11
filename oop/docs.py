# Строка документации модуля

print(__builtins__.__doc__)   # Модуль докстроки
# Built-in functions, exceptions, and other objects.
# Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.

# Строка документации функции

print(dir.__doc__)   # Function docstring

print (isinstance.__doc__)
# isinstance(object, class-or-type-or-tuple) -> Boolean

# Return whether an object is an instance of a class or of a subclass thereof.
# With a type as second argument, return whether that is the object's type.
# The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for
# isinstance(x, A) or isinstance(x, B) or ... (etc.).[33]


# Строки документации класса и метода

class Mat:
    """Mathematical function for the vertical motion of a ball.

    Methods:
       constructor(v0): set initial velocity v0.
       value(t): compute the height as function of t.
       formula(): print out the formula for the height.

    Attributes:
       v0: the initial velocity of the ball (time 0).
       g: acceleration of gravity (fixed).
    """
    def formula(self):
        """formula(): print out the formula for the height."""

        pass


print(Mat.__doc__)   # Докстрока класса

print(Mat.formula.__doc__)   # Докстрока метода класса

