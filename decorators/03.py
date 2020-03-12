# Функция another_function является функцией декоратором. 
# Декоратор модифицирует функцию, которая передается в качестве параметра
# Декоратор возвращает модифицированную функцию. 

def another_function(func):
   """  Функция которая принимает другую функцию.   """
   def other_func():
       val = "Результат от %s это %s" % (func(), eval(func()) )
       return val
   return other_func

# Декоратор начинается с символа @, за которым следует название функции, которую мы собираемся декорировать. 
# Для применения декоратора нужно разместить его в строке перед определением функции. 

@another_function
def a_function():
   """Обычная функция"""
   return "1+1"

if __name__ == "__main__":
   value = a_function()
   print(value)
