# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''

import glob
import re
import csv

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

def parse_sh_version(line_of_sh_version):
    result1 = []
    ios_regex = re.compile('Cisco IOS Software, \S+?\s+\S+?\s+\S+?\s+Version (\S+?),')
    uptime_regex = re.compile('uptime is (\d+ days, \d+ hours, \d+ minutes)')
    image_regex = re.compile('System image file is "(\S+?)"')
    match1 = ios_regex.search(line_of_sh_version)
    match3 = uptime_regex.search(line_of_sh_version)
    match2 = image_regex.search(line_of_sh_version)
    if match1:
        ios = match1.group(1)
        result1.append(ios)
    if match2:
        image = match2.group(1)
        result1.append(image)
    if match3:
        uptime = match3.group(1)
        result1.append(uptime)
    result = tuple(result1)
    return result

def write_inventory_to_csv(data_filenames, csv_filename):
    result = []
    result.append(headers)
    for filename in data_filenames:
        with open(filename, 'r') as f:
            filename1 = f.read()
            result1 = []
            name_regex = re.compile('sh_version_(\S+).txt')
            match = name_regex.search(filename)
            tuple1 = parse_sh_version(filename1)
            if match:
                hostname = match.group(1)
                result1.append(hostname)
            for item in tuple1:
                result1.append(item)
            result.append(result1)
    with open(csv_filename,'w') as w:
        writer = csv.writer(w)
        for row in result:
            writer.writerow(row)

if __name__=='__main__':
    write_inventory_to_csv(sh_version_files, 'routers_inventory.csv')
