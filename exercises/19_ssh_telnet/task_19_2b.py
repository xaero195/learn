# -*- coding: utf-8 -*-
'''
Задание 19.2b

Скопировать функцию send_config_commands из задания 19.2a и добавить проверку на ошибки.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве, например:
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1

Ошибки должны выводиться всегда, независимо от значения параметра verbose.
При этом, verbose по-прежнему должен контролировать будет ли выводиться сообщение:
Подключаюсь к 192.168.100.1...


Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.


Пример работы функции send_config_commands:

In [16]: commands
Out[16]:
['logging 0255.255.1',
 'logging',
 'i',
 'logging buffered 20010',
 'ip http server']

In [17]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Команда "i" выполнилась с ошибкой "Ambiguous command:  "i"" на устройстве 192.168.100.1

In [18]: pprint(result, width=120)
({'ip http server': 'config term\n'
                    'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                    'R1(config)#ip http server\n'
                    'R1(config)#',
  'logging buffered 20010': 'config term\n'
                            'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                            'R1(config)#logging buffered 20010\n'
                            'R1(config)#'},
 {'i': 'config term\n'
       'Enter configuration commands, one per line.  End with CNTL/Z.\n'
       'R1(config)#i\n'
       '% Ambiguous command:  "i"\n'
       'R1(config)#',
  'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

In [19]: good, bad = result

In [20]: good.keys()
Out[20]: dict_keys(['logging buffered 20010', 'ip http server'])

In [21]: bad.keys()
Out[21]: dict_keys(['logging 0255.255.1', 'logging', 'i'])


Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#i
% Ambiguous command:  "i"
'''
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
