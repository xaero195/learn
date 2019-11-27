# -*- coding: utf-8 -*-
'''
Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

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

def parse_output_to_dict(template, command_output):
    result = [] 
    body = [list(row) for row in cli_table]
    header = list(cli_table.header)
    lenght_header = len(header)
    lenght_body = len(body)
    for i in range(lenght_body):
        result1 = {}
        for j in range(lenght_header):
            result1[header[j]]=body[i][j]
        result.append(result1)
    return result

if __name__=='__main__':
    with open('output/sh_ip_int_br.txt') as o:
        output = o.read()
        print(parse_command_output('templates/sh_ip_int_br.template', output))
        print(parse_output_to_dict('templates/sh_ip_int_br.template', output))
