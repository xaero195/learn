# -*- coding: utf-8 -*-
'''
Задание 22.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами. Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - templates

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
'''

from task_22_1a import parse_output_to_dict
from textfsm import clitable

attributes = {'Command': 'sh ip int br', 'Vendor': 'Cisco'}

def parse_command_dynamic(command_output, attributes_dict, index_file='index', templ_path='templates'):
    result = []
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes)
    body = [list(row) for row in cli_table]
    header = list(cli_table.header)
    lenght_header = len(header)
    lenght_body = len(body)
    for i in range(lenght_body):
        result1 = {}
        for j in range(lenght_header):
            result1[header[j]]=body[i][j]
        result.append(result1)
  #  result = parse_output_to_dict(cli_table ,command_output)
    return result


if __name__=='__main__':
    with open('output/sh_ip_int_br.txt') as o:
        output = o.read()
        print(parse_command_dynamic(output, attributes))
        
