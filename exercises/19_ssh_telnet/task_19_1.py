# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

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
    
    with ConnectHandler(**device) as ssh:
        ssh.enable()

        result = ssh.send_command(command)
#        print(result)
    return result

with open(filename) as f:
    devices = yaml.safe_load(f)
for item in devices:
    print(send_show_command(item, command))

    



