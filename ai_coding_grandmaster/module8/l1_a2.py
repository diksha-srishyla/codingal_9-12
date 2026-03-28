#empty dictionary
my_dict = {}

#dictionary with integer keys
my_dict = {1: 'apple', 2:'banana'}

#dictionary with mixed keys
my_dict = {'name':'John', 'age':26}

#Output: Jack
print(my_dict['name'])
print(my_dict.get('age'))

#update value
my_dict['age'] = 27
print(my_dict)

#remove particular element
my_dict.pop('age')
print(my_dict)

#access a particular element
print("Address:", my_dict.get('address'))

#remove all the elements
my_dict.clear()
print(my_dict)