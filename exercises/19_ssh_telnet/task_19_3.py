# -*- coding: utf-8 -*-
'''
Задание 19.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к устройству, которому надо передать команды
* show - одна команда show (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В зависимости от того, какой аргумент был передан, функция вызывает разные функции внутри.
При вызове функции send_commands, всегда будет передаваться только один из аргументов show, config.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 19.1
* config - функция send_config_commands из задания 19.2

Функция возвращает строку с результатами выполнения команд или команды.

Проверить работу функции:
* со списком команд commands
* командой command

Пример работы функции:

In [14]: send_commands(r1, show='sh clock')
Out[14]: '*17:06:12.278 UTC Wed Mar 13 2019'

In [15]: send_commands(r1, config=['username user5 password pass5', 'username user6 password pass6'])
Out[15]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#username user5 password pass5\nR1(config)#username user6 password pass6\nR1(config)#end\nR1#'
'''


import getpass
import sys
from netmiko import ConnectHandler
import yaml
import re

#command = sys.argv[1]
#user = input('Username: ')
#password = getpass.getpass()
#enable_pass = getpass.getpass(prompt='Enter enable password: ')
#devices_ip = ['192.168.100.1', '192.168.100.2', '192.168.100.3']
filename = 'devices.yaml'
commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]
command = 'sh ip int br'

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
    good = {}
    bad = {}
    regex_err_invalid = re.compile(r'\S+Invalid input detected\S+')
    regex_err_incomplete = re.compile(r'\S+Incomplete command\S+')
    regex_err_ambiguous = re.compile(r'\S+Ambiguous command\S+')
    for command in config_commands:

        try:
            if verbose:
                print('Try to connect with {}'.format(device[ip]))
            with ConnectHandler(**device) as ssh:
                ssh.enable()
    
                result_source = ssh.send_command(command)

                match_invalid = regex.search(result_source)
                match_incomplete = regex.search(result_source)
                match_ambiguous = regex.search(result_source)
                if match_invalid:
                    print('ALARM! Invalid on {}!'.format(device[ip]))
                    bad.update(command:match_invalid.groups())
                    answer = input('Continue? [y/n]')
                    if answer == 'n':
                        break
                        answer = ''
                elif match_incomplete:
                    print('ALARM! Incomplete on {}!'.format(device[ip]))
                    bad.update(command:match_incomplete.groups())
                    answer = input('Continue? [y/n]')
                    if answer == 'n':
                        break
                        answer = ''
                elif match_ambiguous:
                    print('ALARM! Ambiguous on {}!'.format(device[ip]))
                    bad.update(command:match_ambiguous.groups())
                    answer = input('Continue? [y/n]')
                    if answer == 'n':
                        break
                        answer = ''
                else:
                    good.update(command:result_source)
            result = tuple(good, bad)
#           print(result)
        except error_authen:
            print('ERROR PASSWORD, ITIT KOLOTIT!')
        except ip_address:
            print('ERROR IP, ITIT KOLOTIT!')
    return result

def show_commands(device, show=False, config=False):
    if show:
        result = send_show_command(device,show)
    elif config:
        result = send_config_commands(device, config)
    return result

with open(filename) as f:
    devices = yaml.safe_load(f)
for item in devices:
    print(show_commands(item, config=commands, show=command))
