# Creating an empty Dictionary 
Dict = {} 
print(f"Empty Dictionary: {Dict}") 

# Adding elements one at a time 
Dict[0] = 'Cats'
Dict[2] = 'Dogs'
Dict[3] = 1
print(f"\nDictionary after adding 3 elements: {Dict}") 

# Creating a Dictionary with Integer Keys 
Dict1 = {1: 'Dogs', 2: 'For', 3: 'Cats'} 
print(f"\nDictionary with the use of Integer Keys: {Dict1}") 

# Creating a Dictionary with Mixed keys 
Dict2 = {'Name': 'Cats', 1: [1, 2, 3, 4]} 
print(f"\nDictionary with the use of Mixed Keys: {Dict2}") 

  
# Creating a Dictionary with dict() method 
Dict3 = dict({1: 'Cats', 2: 'For', 3:'Dogs'}) 
print(f"\nDictionary with the use of dict(): {Dict3}")
  
# Creating a Dictionary with each item as a Pair 
Dict4 = dict([(1, 'Cats'), (2, 'Dogs')]) 
print(f"\nDictionary with each item as a pair: {Dict4}") 


# Accessing an element from a Dictionary 
Dict5 = {1: 'Dogs', 'name': 'For', 3: 'Cats'}

# accessing an element using key
print(f"Accessing a {Dict5['name']} element using key: {'name'}")
print(f"Accessing a {Dict5[1]} element using key: {1}")
# accessing a element using get() method 
print(f"Acessing a {Dict5.get(3)} element using get by key {3}:") 

# Add new keys to a dictionary: Using Subscript notation
dict = {'key1':'Cow', 'key2':'fill_me'} 
print("Current Dict is: ", dict) 
  
# Dictionary_Name[New_Key_Name] = New_Key_Value 
dict['key2'] = 'for'
dict['key3'] = 'rats'
print("Updated Dict is: ", dict) 


# Python 3.6 and beyond
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
print(a_dict) # {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
print(a_dict) # {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

for key in a_dict:
    print(key)

for key in a_dict:
   print(key, a_dict[key])

# ############### Nested Key value ############
# Creating a Nested Dictionary
Dict = {1: 'Cats', 2: 'For',  
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Home'}} 
print(Dict)  


# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Cats'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 

# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Zoo', 
        'A' : {1 : 'Dogs', 2 : 'For', 3 : 'Rats'}, 
        'B' : {1 : 'Cats', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 

#####################
# Using loops
# Pretty Print a dictionary with dictionary value Using loops 
# initializing dictionary 
test_dict = {'rats' : {'rate' : 5, 'remark' : 'good'}, 'cats' : {'rate' : 3}} 
  
print("The original dictionary is : " +  str(test_dict)) 
  
# using loops to Pretty Print 
print("The Pretty Print dictionary is : ") 
for sub in test_dict: 
    print (sub) 
    for sub_nest in test_dict[sub]: 
        print (sub_nest, ':', test_dict[sub][sub_nest]) 


a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
print(a_dict)
d_items = a_dict.items()
print(d_items) # Here d_items is a view of items
# dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])

for item in a_dict.items():
    print(item)

for val in a_dict.values():
   print(val)

nums = {3: 'three', 4: 'four'}
nums.update({6: 'six', 7: 'seven'}) # {3: 'three', 4: 'four', 6: 'six', 7: 'seven'}

num1 = {5: 'foo', 6: 'bar'}

nums.update(num1) # пополняем словарь из другого словаря
print(nums)
# Количество пар в хеше
print(len(nums)) # количество пар ключ-значение

def del_elem(id):
    del nums[id] 

del_elem(5)
print(nums)

def pop_elem(id):
    return nums.pop(id) 
remove_elem = pop_elem(6)
print(f'Element {remove_elem} Removed Successfully!')


# def del_elem(id):
#     # проверка наличия ключа
#     if id in nums:
#         del nums[id] 

# def pop_elem(id):
#     # проверка наличия ключа
#     if id in nums:
#             return nums.pop(id) 
# remove_elem = pop_elem(6)

