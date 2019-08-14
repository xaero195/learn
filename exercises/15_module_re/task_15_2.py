# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

'''
import re

def parse_sh_ip_int_br(filename):
    result = []
    regex1 = re.compile('(\S+) +(\S+) +YES +(manual|unset)\s+(.+?)\s+(\S+$)')
   # regex2 = re.compile('ip address (\d+.\d+.\d+.\d+) +(\d+.\d+.\d+.\d+)')
    with open(filename) as f:
        for line in f:
            match1 = regex1.search(line)
            if match1:
                list_of_ip = [match1.group(1),match1.group(2),match1.group(4),match1.group(5)]
                tuple1 = tuple(list_of_ip)
                result.append(tuple1)
                #r1 = dict(())
               # result.update({key_interface: list_of_ip2})
    return result

if __name__=="__main__":
    print(parse_sh_ip_int_br('sh_ip_int_br.txt'))
