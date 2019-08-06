# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''
import subprocess
import ipaddress
from tabulate import tabulate

def ping_ip_addresses(ip_addresses):
    result1 = []
    result2 = []
    for ip_address in ip_addresses:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip_address],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               encoding='utf-8')
        if reply.returncode == 0:
            result1.append(ip_address)
        else:
            result2.append(ip_address)
    result = tuple([result1,result2])
    return result

def convert_ranges_to_ip_list(list_of_ip_addresses):
    result=[]
    for item in list_of_ip_addresses:
        source = item.split('-')
        if len(source) == 1:
            result.append(source[0])
        else:
            k = 0
            source2 = source[0].split('.')
            m = int(source2[3])
            if len(source[1]) == 1:
                k = int(source[1])
            else:
                source1 = source[1].split('.')
                k = int(source1[3])
            ip1 = ipaddress.ip_address(source[0])
            for i in range(m, k+1):
                result.append(str(ip1))
                ip1 += 1
    return result

columns = ['Reachable', 'Unreachable']
sh_ip = ping_ip_addresses(convert_ranges_to_ip_list(['8.8.4.4', '172.19.30.1-172.19.30.254']))
print(tabulate(sh_ip, headers=columns))
