# -*- coding: utf-8 -*-
'''
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

'''
import yaml
from jinja2 import Environment, FileSystemLoader
import sys
import os

template_path = 'templates/for.txt'
data_path = 'data_files/for.yml'

def generate_config(template, data_dict):
    template_dir, template_file = os.path.split(template)
    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True)
    template_final = env.get_template(template_file)

    with open(data_dict) as f:
        vars_dict = yaml.safe_load(f)

    return template_final.render(vars_dict)


if __name__=='__main__':
    print(generate_config(template_path, data_path))
