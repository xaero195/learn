# -*- coding: utf-8 -*-
'''
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
'''

import getpass
import sys
from netmiko import ConnectHandler
import yaml

#command = sys.argv[1]
#user = input('Username: ')
#password = getpass.getpass()
#enable_pass = getpass.getpass(prompt='Enter enable password: ')
#devices_ip = ['192.168.100.1', '192.168.100.2', '192.168.100.3']
filename = 'devices.yaml'
command = 'sh ip int br'

def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()

            result = ssh.send_command(command)
#        print(result)
    except ERROR!!!:
        print('ERROR ITIT KOLOTIT!')
        
    return result

with open(filename) as f:
    devices = yaml.safe_load(f)
for item in devices:
    print(send_show_command(item, command))
