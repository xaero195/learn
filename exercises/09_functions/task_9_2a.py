# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

def generate_trunk_config(intf_vlan_mapping, trunk_template, psecurity=None):
    finish_list = {key: [] for key in intf_vlan_mapping}
    for key in intf_vlan_mapping:
        for item in trunk_template:
            if item.endswith('vlan'):
                finish_list[key].append((item+' '+str(','.join([str(intf_vlan) for intf_vlan in intf_vlan_mapping[key]])).rstrip()))
            else:
                finish_list[key].append(item.rstrip())
        if psecurity:
            for item2 in psecurity:
                finish_list[key].append(item2.rstrip())
    return finish_list
print(generate_trunk_config(trunk_config, trunk_mode_template))
