# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.


import random
numberN_set = set(random.randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(numberN_set)
numberM_set = set(random.randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(numberM_set)
same_set = sorted(numberN_set.intersection(numberM_set))
print(*same_set)
