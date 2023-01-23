from view import view_data
import os

def data_write(fullname, number, description):
    with open('base.txt', 'a') as file:
        file.write(f'{fullname}:{number}:{description}\n')

def data_read_base():
    with open('base.txt', 'r') as file:
        base = [line.split(':') for line in file]
    return base

def find_data(desired):
    base = data_read_base()
    finded = []
    for item in base:
        try:
            if desired.lower() in item[0].lower() or desired in item[1]:
                finded.append(item)
        except:
            continue
    return finded

def delete_data(finded):
    for i in finded:
        print('Найдена запись: ')
        view_data(i[0], i[1], i[2])
        des = int(input('1 - удалить её, 0 - не удалять: '))
        if des == 1:
            os.rename('base.txt', 'tmp_base.txt')
            with open('tmp_base.txt', 'r') as file:
                for line in file:
                    if line != f'{str(i[0])}:{str(i[1])}:{str(i[2])}':
                        with open('base.txt', 'a') as f:
                            f.write(line)
            os.remove('tmp_base.txt')
