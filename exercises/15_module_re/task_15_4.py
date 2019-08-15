# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''
import re

def get_ints_without_description(filename):
    result = []
    regex1 = re.compile('^interface (\S+)')
    regex2 = re.compile('^ description')
    with open(filename) as f:
        for line in f:
            match1 = regex1.search(line)
            if match1:
                interface = match1.group(1)
                result.append(interface)
            match2 = regex2.search(line)
            if match2:
                result.pop()
    return result

if __name__=='__main__':
    print(get_ints_without_description('config_r1.txt'))
