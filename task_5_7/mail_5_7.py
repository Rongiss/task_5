CONST_SECTOR_A = 20
CONST_SECTOR_B = 15
CONST_SECTOR_C = 10
list_sector = ['A', 'B', 'C']

def main_5_7():
    var_sector = 0
    total = 0

    for i in range(3):
        print('\nВвведите данные сектора ', list_sector[var_sector])
        sactor = list_sector[var_sector]
        total += calculate(sactor, input_amount_place())
        var_sector += 1

    print('Итоговая сумма равна -', total, sep=' ')

def calculate(sector ,how_place):
    if sector == 'A':
        result = how_place * 20
    elif sector == 'B':
        result = how_place * 15
    elif sector == 'C':
        result = how_place * 10
    return result


def input_amount_place():
    how_place = int(input('Введите количество приобретенных мест - '))

    while how_place < 0:
        print('Выдопустили ошибку, число мест не может быть отрицательным')
        print('Повторите попытку')
        how_place = int(input('Введите количество приобретенных мест - '))
    return how_place


main_5_7()