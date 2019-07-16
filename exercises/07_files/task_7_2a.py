# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv
ignore = ['duplex', 'alias', 'Current configuration']
filename = argv[1]
with open(filename, 'r') as fn:
    for line in fn:
        if line[0]=='!':
            continue
        else:
            for word in ignore:
                if word in line:
                    break
            else:
                print(line.rstrip())

        

