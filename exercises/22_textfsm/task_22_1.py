# -*- coding: utf-8 -*-
'''
Задание 22.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.

'''

import sys
import textfsm
from tabulate import tabulate

def parse_command_output(template, command_output):
    with open(template) as f:
        re_table = textfsm.TextFSM(f)
        header = re_table.header
        body = re_table.ParseText(command_output)
        body.insert(0, header)
        result = body
    return result

if __name__=='__main__':
    with open('output/sh_ip_int_br.txt') as o:
        output = o.read()
        print(parse_command_output('templates/sh_ip_int_br.template', output))
        
