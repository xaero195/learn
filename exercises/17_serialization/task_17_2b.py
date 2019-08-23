# -*- coding: utf-8 -*-
'''
Задание 17.2b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_2b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
import yaml
from draw_network_graph import draw_topology

def transform_topology(filename):
    result = {}
    result1 = {}
    with open(filename, 'r') as f:
        temp = yaml.load(f)
        for key in temp:
            temp1 = temp[key]
            for key1 in temp1:
                temp2 = temp1[key1]
                for key2 in temp2:
                    temp3 = [key2, temp2[key2]]
                    temp4 = tuple(temp3)
                tempdict = [key, key1]
                temptuple = tuple(tempdict)
                tempdict2 = {temptuple: temp4}
                result1.update(tempdict2)
    keys_result = set(result1.keys())
    key_result = []
    for key3 in keys_result:
        result2 = {}
        if not (result1[key3] in key_result):
            key_result.append(key3)
            result2 = {key3: result1[key3]}
            result.update(result2)
    return result

if __name__=='__main__':
    draw_topology(transform_topology('topology.yaml'))

