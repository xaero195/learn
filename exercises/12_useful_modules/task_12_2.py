# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''
#import subprocess
import ipaddress

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

print(convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']))
