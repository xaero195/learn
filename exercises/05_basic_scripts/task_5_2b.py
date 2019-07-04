# -*- coding: utf-8 -*-
from sys import argv
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#ip_net = input('input ip-network like a.a.a.a/b ')
ip_net = argv[1]
help1 = ip_net.split('/')
help2 = help1[0].split('.')
help2[3] = 0
help3 = int(help1[1])
help4 = 32 - help3
mask = str('1'*help3) + str('0'*help4)

print('Network:\n{:<12}{:<12}{:<12}{:<12}'.format(int(help2[0]),int(help2[1]),int(help2[2]),int(help2[3])))
print('{:<08b}    {:<08b}    {:<08b}    {:<08b}'.format(int(help2[0]),int(help2[1]),int(help2[2]),int(help2[3])))
print('\n')
print('Mask:\n/{}'.format(help1[1]))
print('{:<12}{:<12}{:<12}{:<12}'.format(int(mask[0:8],2),int(mask[8:16],2),int(mask[16:24],2),int(mask[24:32],2)))
print('{:<08}    {:<08}    {:<08}    {:<08}'.format(int(mask[0:8]),int(mask[8:16]),int(mask[16:24]),int(mask[24:32])))
