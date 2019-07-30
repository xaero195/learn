# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def parse_cdp_neighbors(command_output):
    result = {}
    com_out = command_output.split()
    full_count = 0-(len(com_out))
    first_elem1 = com_out[0].split('>')
    first_elem = first_elem1[0]
    counter = 2
    for k in range(-1, full_count, -1):
        if 'ID' in com_out[k]:
            break
        elif '/' in com_out[k] and counter == 2:
            elem2 = com_out[k-1]+com_out[k]
            counter = 1
        elif '/' in com_out[k] and counter == 1:
            elem1 = com_out[k-1]+com_out[k]
            counter = 2
            switch_elem = com_out[k-2]
            list1 = [first_elem, elem1]
            tuple1 = tuple(list1)
            list2 = [switch_elem, elem2]
            tuple2 = tuple(list2)
            result1 = {tuple1: tuple2}
            result.update(result1)
    return result
                


#with open('sh_cdp_n_sw1.txt', 'r') as sc:
 #   source = sc.read()
  #  print(parse_cdp_neighbors(source))
