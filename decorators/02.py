def a_function():
   """Обычная функция"""
   return "1+1"

# another_function функция принимает один аргумент, этот аргумент является функцией. 
# another_function функция содержит вложенную функцию other_func. 

def another_function(func):
   """  Функция которая принимает другую функцию.   """
   def other_func():
       val = "Результат от %s это %s" % (func(), eval(func()) )
       return val
   return other_func

# Функция another_function является функцией декоратором. 
# Декоратор модифицирует функцию, которая передается в качестве параметра
# Декоратор возвращает модифицированную функцию. 

if __name__ == "__main__":
   value = a_function()
   print(value)
   decorator = another_function(a_function)
   print(decorator())
