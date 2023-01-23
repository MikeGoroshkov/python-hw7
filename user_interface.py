import view
import data_base

def start():
    while True:
        print('\n')
        operation = int(input("Выберите операцию со справочником:\n1 - запись в справочник\n2 - вывод на экран всего справочника"
                              "\n3 - поиск по справочнику\n4 - удаление из справочника\nq - выход из программы\n: "))
        if operation == 1:
            fullname = view.input_data("Введите имя: ")
            number = view.input_data("Введите номер телефона в формате 89991234567: ")
            description = view.input_data("Введите описание: ")
            data_base.data_write(fullname, number, description)
        if operation == 2:
            full_base = data_base.data_read_base()
            view.view_base(full_base)
        if operation == 3:
            desired = view.input_data("Введите искомое имя, фамилию или ФИО целиком или искомый номер: ")
            finded = data_base.find_data(desired)
            view.view_base(finded)
        if operation == 4:
            desired = view.input_data("Введите искомое имя, фамилию или ФИО целиком или искомый номер: ")
            finded = data_base.find_data(desired)
            data_base.delete_data(finded)
        if operation == 'q' or operation == 'й':
            break

