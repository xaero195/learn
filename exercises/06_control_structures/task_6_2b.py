# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
a=1
while a==1:
    ip_adres = input('ввод IP-адреса в формате 10.0.1.1: ')
    try:
        octets = ip_adres.split('.')
        if len(octets)==4:
            if 0<=int(octets[0])<=255 and 0<=int(octets[1])<=255 and 0<=int(octets[2])<=255 and 0<=int(octets[3])<=255:
                if 1<=int(octets[0])<=223:
                    print('unicast')
                    a=2
                elif 224<=int(octets[0])<=239:
                    print('multicast')
                    a=2
                elif int(octets[0])==255 and int(octets[1])==255 and int(octets[2])==255 and int(octets[3])==255:
                    print('local broadcast')
                    a=2
                elif int(octets[0])==0 and int(octets[1])==0 and int(octets[2])==0 and int(octets[3])==0:
                    print('unassigned')
                    a=2
                else:
                    print('unused')
                    a=2
            else:
                continue
        else:
            continue
    except:
        print('Неправильный IP-адрес')
