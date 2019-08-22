# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re

def parse_sh_cdp_neighbors(source_line):
    name_dev_regex = re.compile('(\S+)>show')
    interface_regex = re.finditer('(\S+) +(Fa|Eth +\S+) +\.?+(Fa|Eth \S+)',source_line)
    match_dev = name_dev_regex.search(source_line)
    print(interface_regex)
    if match_dev:
        key = match_dev.group(1)
    if interface_regex:
        dict3 = {}
        for match in interface_regex:
            print(match)
            dict1 = {match.group(1): match.group(3)}
            dict2 = {match.group(2): dict1}
            dict3.append(dict2)
        dict4 = {key: dict3}
    return dict4

if __name__=='__main__':
    with open('sh_cdp_n_sw1.txt','r') as f:
        line = f.read()
        print(parse_sh_cdp_neighbors(line))
