# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
num_vlan = input('Type number VLAN: ')
sort_vlans_list = list()
with open('CAM_table.txt','r') as mac:
    for line in mac:
        line_list = line.split()
        try:
            vlan = int(line_list[0].rstrip())
            if num_vlan == vlan:
                sort_vlans_list.append(line_list)
#            print(line.rstrip())
        except:
            continue
sort_vlans_list = sorted(sort_vlans_list, key=lambda vlan: int(vlan[0]))
#sort_vlans_list = '/n'.join(sort_vlans_list)
for item in sort_vlans_list:
    item = '    '.join(item)
    print(item)
