# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_net = input('input ip-network like a.a.a.a/b ')
help1 = ip_net.split('/')
help2 = help1[0].split('.')
help3 = int(help1[1])
help4 = 32 - help3
mask = str('1'*help3) + str('0'*help4)

print('Network:\n{:<12}{:<12}{:<12}{:<12}'.format(int(help2[0]),int(help2[1]),int(help2[2]),int(help2[3])))
print('{:<08b}    {:<08b}    {:<08b}    {:<08b}'.format(int(help2[0]),int(help2[1]),int(help2[2]),int(help2[3])))
print('\n')
print('Mask:\n/{}'.format(help1[1]))
print('{:<12}{:<12}{:<12}{:<12}'.format(int(mask[0:8],2),int(mask[8:16],2),int(mask[16:24],2),int(mask[24:32],2)))
print('{:<12}{:<12}{:<12}{:<12}'.format(int(mask[0:8]),int(mask[8:16]),int(mask[16:24]),int(mask[24:32])))

