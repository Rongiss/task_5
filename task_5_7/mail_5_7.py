

# Константы цены билетов за метосто в секторе
CONST_SECTOR_A = 20
CONST_SECTOR_B = 15
CONST_SECTOR_C = 10

# Обьявляю список секторов
list_sector = ['A', 'B', 'C']


# Объявляю главную функцию
def main_5_7():
    # Переменная для смены сектора в цикле for
    var_sector = 0
    # Переменная подсчета общей суммы
    total = 0

    # Цикл замены сектора в сообщении
    for i in range(3):
        on_sector = 0
        # Вывод информации о секторе в котором были приобретены билеты
        print('\nВвведите данные сектора ', list_sector[var_sector])
        # Присвоение перменной значения из списка для передачи в фукцию подсчета
        sactor = list_sector[var_sector]
        # Переменная аккумулирующая значения полученные из фуннкции подсчета
        on_sector += calculate(sactor, input_amount_place())
        total += on_sector
        print('\nСумма с сектора ', list_sector[var_sector], 'равна', on_sector)
        # Переменная для прохождения итераций цикла
        var_sector += 1
    # Вывод итоговой суммы
    print('\nИтоговая сумма равна -', total, sep=' ')


# Объявляю функцию подсчета
def calculate(sector ,how_place):
    # Ветвление для подчета суммы по секторам
    if sector == 'A':
        result = how_place * 20
    elif sector == 'B':
        result = how_place * 15
    elif sector == 'C':
        result = how_place * 10
    # Возвращаемое значение в аккумклируемую переменную
    return result


# Функция ввода количества проданных мест
def input_amount_place():
    # Ввод данных пользователем
    how_place = int(input('Введите количество приобретенных мест - '))
    # Валидация введенных данных пользователем
    while how_place < 0:
        print('Выдопустили ошибку, число мест не может быть отрицательным')
        print('Повторите попытку')
        how_place = int(input('Введите количество приобретенных мест - '))
    # Возвращаемое знаачение о количестве мест в секторе
    return how_place




# Вызов главной функции
main_5_7()