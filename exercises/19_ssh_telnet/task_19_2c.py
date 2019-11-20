# -*- coding: utf-8 -*-
'''
Задание 19.2c

Скопировать функцию send_config_commands из задания 19.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

'''

# списки команд с ошибками и без:
commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands

import re

# списки команд с ошибками и без:
commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands

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
