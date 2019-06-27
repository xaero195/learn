# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'OSPF      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split()

print("{:23} {:23}".format("Protocol:", ospf_route[0]))
print("{:23} {:23}".format("Prefix:", ospf_route[1]))
print("{:23} {:23}".format("AD/Metric:", ospf_route[2].strip('[]')))
print("{:23} {:23}".format("Next-Hop:", ospf_route[4].strip(',')))
print("{:23} {:23}".format("Last update:", ospf_route[5].strip(',')))
print("{:23} {:23}".format("Outbound Interface:", ospf_route[6]))
