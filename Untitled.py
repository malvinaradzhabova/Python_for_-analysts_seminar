#!/usr/bin/env python
# coding: utf-8

# ## Задание 1
# 
# 1.1 Соедините два словаря в один
# 
# dict1 = {'One': 1, 'Two': 2, 'Three': 3}
# 
# dict2 = {'Four': 4, 'Five': 5, 'Six': 6}
# 
# 1.2 Напишите функцию, которая на вход принимает два словаря и возвращает один объединенный словарь.
# Используйте аннотирование типов
# 

# In[1]:


dict1 = {'One': 1, 'Two': 2, 'Three': 3}
dict2 = {'Four': 4, 'Five': 5, 'Six': 6}


# In[2]:


def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1

merge_dicts(dict1, dict2)


# ## Задание 2

# Напишите, которая из двух списков, делает один словарь, 
# где элементы из первого списка - ключи, а элементы из второго списка - значения
# 
# keys = ['One', 'Two', 'Three']
# 
# values = [1, 2, 3]
# 
# Используйте аннотирование типов
# 

# In[10]:


keys = ['One', 'Two', 'Three']
values = [1, 2, 3]


# ### 2.1 Используя цикл for

# In[13]:


def get_dict(keys, values):
    res_dict = {}
    for i in range (len(keys)):
        res_dict.update({keys[i]: values[i]})
    return res_dict

get_dict(keys, values)


# ### 2.2 Используя dict comprehensions

# In[14]:


def get_dict(keys, values):
    return{keys[i]: values[i]  for i in range (len(keys))}

get_dict(keys, values)


# ## Задание 3

# Извлеките только два ключа name и age из представленного словаря
# client_dict = {
# "name": "John",
# "age": 25,
# "salary": 5000,
# "city": "Moscow"
# }

# ### 3.1 Напишите функцию с циклом for
# Функция на вход принимает:
# - исходный словарь
# - ключи, которые нужно извлечь (аргумент по умолчанию)
# 
# На выходе словарь с нужными ключами
# 
# Используйте аннотирование типов
# 

# In[16]:


client_dict = {
"name": "John",
"age": 25,
"salary": 5000,
"city": "Moscow"
}


# In[17]:


keys = ['name', 'age']


# In[21]:


def get_keys(base_dict, keys: list = ['name', 'age']):
    res_dict = {}
    for i in keys:
        res_dict.update({i: base_dict[i]})
    return res_dict

get_keys(client_dict)


# ### 3.2 Используя dict comprehensions

# In[22]:


new_dict = {i: client_dict[i] for i in keys}
new_dict


# ## Задание 5

# ### 5.1 Найдите картинку в интернете и прикрепите её в ячейку с текстом
# 

# <img src = 'https://cdn.playcaliber.com/site/media/news/2021/06/01/4-%D0%A2%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0-%D0%BC%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B0%D1%8F-%D0%BF%D0%BE-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B0%D0%BC-1280%D1%85853.jpg'>

# <img src = 'https://cdn.playcaliber.com/site/media/news/2021/06/01/4-%D0%A2%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0-%D0%BC%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B0%D1%8F-%D0%BF%D0%BE-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B0%D0%BC-1280%D1%85853.jpg'>

# ### 5.2 Создайте следующую таблицу в ячейке с текстом

# <table>
# <tr>
# <td> </td>
# <td>До события</td>
# <td>Во время события</td>
# </tr>
# <tr>
# <td>1 контрольная точка</td>
# <td>250</td>
# <td>500</td>
# </tr>
# <tr>
# <td>2 контрольная точка</td>
# <td>350</td>
# <td>700</td>
# </tr>
# <tr>
# <td>3 контрольная точка</td>
# <td>400</td>
# <td>800</td>
# </tr>
# <tr>
# <td>Итог за победу</td>
# <td>1000</td>
# <td>2000</td>
# </tr>
# </table>

# ## Задание 6
# Напишите функцию, которая может принимать любое количество трат пользователя и считать сумму и среднее.
# - На вход поступают целочисленные значения в любом количестве
# - На выходе словарь с ключами суммы трат и средней траты
# 

# In[26]:


def calc_purchacses(*args):
    sum_purch = sum(args)
    n_purch = len(args)
    return {
        'sum': sum_purch,
        'mean': sum_purch / n_purch
    }

calc_purchacses(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# ## Задание 4

# ## 4.1 Сгенерируйте случайные целые числа от 0 до 100 в количестве 5 штук с помощью модуля random
# - Зафиксируйте псевдогенерацию, чтобы сгенерированные значения всегда были одинаковые
# - Используйте list comprehensions
# 
# 

# In[31]:


import random
random.seed(3)

numbers = [random.randint(0, 100) for i in range (5)]
numbers


# ## 4.2 Напишите генератор
# - Генератор на вход принимает список с данными о клиенте (данные из пункта 4.1)
# - Внутри генератора реализуйте обход по списку с данными
# На каждой итерации генератор будет возвращать кортеж из двух элементов:
# 1. данные по клиенту (в зависимости от итерации, на 0 итерации вернется 0 элемент, на 1 итерации вернется 1 элемент и тд)
# 2. целочисленное значение, которое показывает, сколько секунд прошло с предыдущей итерации
# Примечание: секунды, которые возвращаются должны показывать время не с начала запуска генератора, а именно то время, которое прошло с предыдущей итерации. А значит время на первой итерации должно равняться 0.
# - Используйте функцию time из модуля time для подсчета времени.
# - Чтобы проверить работу таймера, запустите проход по генератору в цикле с time.sleep(2)
# 

# In[33]:


import time

def func_generator(numbers):
    last_time = None

    for i in numbers:
        current_time = time.time()

        if last_time:
            delta = current_time - last_time
        else:
            delta = current_time - current_time
        last_time = time.time()
        yield (int(delta), i)


# In[34]:


for i in func_generator(numbers):
    print(i)
    time.sleep(2)


# In[ ]:




