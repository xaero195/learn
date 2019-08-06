# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess


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

print(ping_ip_addresses(['8.8.8.8','172.19.30.12','8.8.8.4','127.0.0.1','192.168.1.5']))
print(ping_ip_addresses('a'))
