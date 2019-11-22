# -*- coding: utf-8 -*-
'''
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
'''

from concurrent.futures import ThreadPoolExecutor
import subprocess

ip_list_source = []
limit_source = 3

for i in range(0,255):
    ip_address = '172.19.30.' + str(i)
    ip_list_source.append(ip_address)

def ping(ip_address):
    reply = subprocess.run(['ping', '-c', '3', '-n', ip_address],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                encoding='utf-8')
    if reply.returncode == 0:
        return True
    else:
        return False

def ping_ip_addresses(ip_list, limit=3):
    good = []
    bad = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result1 = executor.map(ping, ip_list)
        for ip, output in zip(ip_list, result1):
            if output:
                good.append(ip)
            else:
                bad.append(ip)
    result = tuple([good, bad])
    return result

if __name__=='__main__':
    print(ping_ip_addresses(ip_list_source, limit_source))




