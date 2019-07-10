# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip_adres = input('ввод IP-адреса в формате 10.0.1.1: ')
try:
    octets = ip_adres.split('.')
    if int(octets[0]) and int(octets[1]) and int(octets[2]) and int(octets[3]) and (not int(octets[4])):
        if 0<=int(octets[0])<=255 and 0<=int(octets[1])<=255 and 0<=int(octets[2])<=255 and 0<=int(octets[3])<=255:
            if 1<=int(octets[0])<=223:
                print('unicast')
            elif 224<=int(octets[0])<=239:
                print('multicast')
            elif int(octets[0])==255 and int(octets[1])==255 and int(octets[2])==255 and int(octets[3])==255:
                print('local broadcast')
            elif int(octets[0])==0 and int(octets[1])==0 and int(octets[2])==0 and int(octets[3])==0:
                print('unassigned')
            else:
                print('unused')
        else:
            print('Неправильный IP-адрес')
    else:
        print('Неправильный IP-адрес')
except:
    print('Неправильный IP-адрес')
