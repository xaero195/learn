# -*- coding: utf-8 -*-

import os
import sqlite3
import sys

db_filename = 'dhcp_snooping.db'

allparam = len(sys.argv)

query_dict = {
    'vlan': 'select vlan, mac, ip, interface, switch, active from dhcp where vlan = ? and active = ?',
    'mac': 'select vlan, mac, ip, interface, switch, active from dhcp where mac = ? and active = ?',
    'ip': 'select vlan, mac, ip, interface, switch, active from where dhcp = ? and active = ?',
    'interface': 'select vlan, mac, ip, interface, switch, active from dhcp where interface = ? and active = ?',
    'switch': 'select vlan, mac, ip, interface, switch, active from dhcp where switch = ? and active = ?'
}


keys = query_dict.keys()

def get_all_tables(filename):
        conn = sqlite3.connect(filename)
        conn.row_factory = sqlite3.Row

        print('\nDetailed information for all hosts')
        print('-' * 40)
        print('active')
        query = 'select * from dhcp where active = 1'
        result = conn.execute(query)
        
        for row in result:
            for row_name in row.keys():
                print('{:12}: {}'.format(row_name, row[row_name]))
            print('-' * 40)
        print('-' * 40)
        print('non-active')
        query = 'select * from dhcp where active = 0'
        result = conn.execute(query)
        
        for row in result:
            for row_name in row.keys():
                print('{:12}: {}'.format(row_name, row[row_name]))
            print('-' * 40)

def get_use_data(filename, key, value):
    if not key in keys:
        print('Enter key from {}'.format(', '.join(keys)))
    else:
        conn = sqlite3.connect(filename)
        conn.row_factory = sqlite3.Row

        print('\nDetailed information for host(s) with', key, value)
        print('-' * 40)
        act = 1
        while act>(-1):
            query = query_dict[key]
            result = conn.execute(query, (value, act, ))
            if act==0:
                print('non-active')
            else:
                print('active')
            for row in result:
                for row_name in row.keys():
                    print('{:12}: {}'.format(row_name, row[row_name]))
                print('-' * 40)
            act=act-1

if allparam == 1:
    get_all_tables(db_filename)
elif allparam == 3:
    key, value = sys.argv[1:]
    get_use_data(db_filename, key, value)
else:
    print('input 0 or 2 parameters!')
