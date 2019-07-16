# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#ospf_route = 'OSPF      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
with open('ospf.txt','r') as ospf_route_file:
    for line in ospf_route_file:
        line = line.split()
        if line[0].strip(' ')=='O':
            print("{:23} {:23}".format("Protocol:", "OSPF"))
        else:
            print("{:23} {:23}".format("Protocol:", "None"))
        print("{:23} {:23}".format("Prefix:", line[1]))
        print("{:23} {:23}".format("AD/Metric:", line[2].strip('[]')))
        print("{:23} {:23}".format("Next-Hop:", line[4].strip(',')))
        print("{:23} {:23}".format("Last update:", line[5].strip(',')))
        print("{:23} {:23}".format("Outbound Interface:", line[6]))
