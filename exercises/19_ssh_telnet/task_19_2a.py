# -*- coding: utf-8 -*-
'''
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр verbose,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

verbose - это параметр функции send_config_commands, не параметр ConnectHandler!

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, verbose=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
'''

import getpass
import sys
import netmiko
import yaml

#command = sys.argv[1]
#user = input('Username: ')
#password = getpass.getpass()
#enable_pass = getpass.getpass(prompt='Enter enable password: ')
#devices_ip = ['192.168.100.1', '192.168.100.2', '192.168.100.3']
filename = 'devices.yaml'
#command = 'sh ip int br'
commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]

def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()

            result = ssh.send_command(command)
#        print(result)
    except error_authen:
        print('ERROR PASSWORD, ITIT KOLOTIT!')
    except ip_address:
        print('ERROR IP, ITIT KOLOTIT!')
    return result

def send_config_commands(device, config_commands, verbose=True):
    try:
        if verbose:
            print('Try to connect with {}'.format(device[ip]))
        with ConnectHandler(**device) as ssh:
            ssh.enable()

            result = ssh.send_config_set(config_commands)
#        print(result)
    except error_authen:
        print('ERROR PASSWORD, ITIT KOLOTIT!')
    except ip_address:
        print('ERROR IP, ITIT KOLOTIT!')
    return result

with open(filename) as f:
    devices = yaml.safe_load(f)
for item in devices:
#    print(send_show_command(item, command))
    print(send_config_commands(item, commands))
