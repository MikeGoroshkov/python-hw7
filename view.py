def view_data(name, number, description):
    print(f'{name} : {number} : {description}')

def input_data(prompt):
    result = input(prompt)
    if not result:
        result = 'нет данных'
    return result

def view_base(base):
    for i in base:
        view_data(i[0], i[1], i[2])