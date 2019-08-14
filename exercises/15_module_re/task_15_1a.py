# -*- coding: utf-8 -*-
'''
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re

def get_ip_from_cfg(filename):
    result = {}
    regex1 = re.compile('interface (\S+)')
    regex2 = re.compile('ip address (\d+.\d+.\d+.\d+) +(\d+.\d+.\d+.\d+)')
    with open(filename) as f:
        for line in f:
            match1 = regex1.search(line)
            if match1:
                key_interface = match1.group(1)
            match2 = regex2.search(line)
            if match2:
                list_of_ip = [match2.group(1),match2.group(2)]
                tuple1 = tuple(list_of_ip)
                #r1 = dict(())
                result.update({key_interface: tuple1})
    return result

if __name__=="__main__":
    print(get_ip_from_cfg('config_r1.txt'))
