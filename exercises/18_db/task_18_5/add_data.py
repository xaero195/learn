import os
import sqlite3
import re
import yaml

data_filenames = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
db_filename = 'dhcp_snooping.db'
switches_filenames = 'switches.yml'

def create_pool_dhcp(data_filename):
    regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    result = []
    regex2 = re.compile('(\S)_\S+.txt')
    for item in data_filename:
        match2 = regex2.search(item)
        if match2:
            

            with open(item) as data:
                for line in data:
                    match = regex.search(line)
                    if match:
                        result1 = [match.group(1), match.group(2), match.group(3), match.group(4), match2.group(1)]
                        result2 = tuple(result1)
                        result.append(result2)
        else:
            print('Error match2!')
    return result

def insert_dhcp(result_pool):
    print('Inserting DHCP Snooping data')
    conn = sqlite3.connect(db_filename)
    query1 = '''update dhcp set active = 0'''
    conn.execute(query1)

    for row in result_pool:
        try:
            with conn: 
                query = '''insert or replace into dhcp (mac, ip, vlan, interface, switch, active, last_active)
                           values (?, ?, ?, ?, ?, 1, datetime('now'))'''
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)

    conn.close()

def insert_switches(switches):
    print('Inserting Switches data')
    conn = sqlite3.connect(db_filename)
    with open(switches) as f:
        sources_switches = yaml.safe_load(f)
        source = sources_switches['switches']
        keys = source.keys()
        result3 = []
        for key in keys:
            list1 = []
            list1.append(key)
            list1.append(source[key])
            tuple1 = tuple(list1)
            result3.append(tuple1)
        for row in result3:
            try:
                with conn:
                    query = '''insert into switches (hostname, location)
                               values (?, ?)'''
                    conn.execute(query, row)
            except sqlite3.IntegrityError as e:
                print('Error occured: ', e)

    conn.close()

if __name__=="__main__":
    pool_dhcp = create_pool_dhcp(data_filenames)
    insert_dhcp(pool_dhcp)
    insert_switches(switches_filenames)
    
