#!/usr/bin/env python3
#método 1 de copiar uma lista:
>>> my_list = ['a', 'bb', 'ccc']
>>> list_copy = my_list
>>> print(my_list)
['a', 'bb', 'ccc']
>>> list_copy.append('dddd')
>>> print(my_list)
['a', 'bb', 'ccc', 'dddd']
>>> print(list_copy)
['a', 'bb', 'ccc', 'dddd']

#método 2 de copiar uma lista:
>>> my_list2 = ['a','bb','ccc']
>>> list_copy2 = my_list2.copy()
>>> print(my_list2)
['a', 'bb', 'ccc']
>>> list_copy2.append('dddd')
>>> print(my_list2)
['a', 'bb', 'ccc']

