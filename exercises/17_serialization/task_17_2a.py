# -*- coding: utf-8 -*-
'''
Задание 17.2a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

'''
import re
import yaml

def parse_sh_cdp_neighbors(source_line):
    name_dev_regex = re.compile('(\S+)>show')
    interface_regex = re.finditer('(\S+)\s+((?:Fa|Eth) \S+).+?((?:Fa|Eth) \S+)',source_line)
    match_dev = name_dev_regex.search(source_line)
    #print(interface_regex)
    if match_dev:
        key = match_dev.group(1)
    if interface_regex:
        dict3 = {}
    for match_int in interface_regex:
        dict1 = {match_int.group(1): match_int.group(3)}
        dict2 = {match_int.group(2): dict1}
        dict3.update(dict2)
    dict4 = {key: dict3}
    return dict4

def generate_topology_from_cdp(list_of_files, save_to_filename = None):
    result1 = {}
    for files in list_of_files:
        with open(files,'r') as f:
            source = f.read()
            dict_parse = parse_sh_cdp_neighbors(source)
            result1.update(dict_parse)
    if save_to_filename:
        with open(save_to_filename, 'w') as w:
            yaml.dump(result1, w)
    return result1

if __name__=='__main__':
    list_files = ['sh_cdp_n_sw1.txt',
                  'sh_cdp_n_r1.txt',
                  'sh_cdp_n_r2.txt',
                  'sh_cdp_n_r3.txt',
                  'sh_cdp_n_r4.txt',
                  'sh_cdp_n_r5.txt',
                  'sh_cdp_n_r6.txt']
    generate_topology_from_cdp(list_files, 'topology.yaml')
