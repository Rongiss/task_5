
CONST_AREA = 10
#СONST_PRICE_COLOR = 35
CONST_WORK_TIME = 8
PRICE_COMPANY = 2000

def main():

    bank, work_time, price_color, price_work, total_price = calculate(input_area_for_work(),input_price_color())

    print('\nКоличество емкостей краски составляет - ', bank)
    print('Время работы составит - ', work_time)
    print('Цена краски равна - ', price_color)
    print('Стоимость работ составляет', price_work)
    print('Итоговая сумма равна - ', total_price)

def input_area_for_work():
    print('\nВведите площадь для покраски')
    area = float(input('Площадь в квадратных метрах составляет - '))
    while area < 0:
        print('Вы допустили ошибку!')
        print('Повторите поппытку ввода площади покраски')
        area = float(input('Площадь в квадратных метрах составляет '))
    return area

def input_price_color():
    print('\nВведите сумму 5-литровой емкости')
    price_color = float(input('Сумма составляет - '))
    while price_color < 0:
        print('Вы допустили ошибку!')
        print('Повторите поппытку ввода суммы')
        price_color = float(input('Сумма составляет - '))
    return price_color

def calculate(area, price_color):

    # Вычисляю количество емкостей
    band = area / CONST_AREA
    if band % 1 > 0:
        band = area // CONST_AREA + 1

    # Часы работы
    time_work = area / CONST_AREA * CONST_WORK_TIME

    # Стоимость краски
    color_money = band * price_color

    # Стоисочть работ
    money_work = time_work * PRICE_COMPANY

    # Общая стоимость
    total_sum = money_work + color_money
    # Возвращау значение
    return band, time_work, color_money, money_work, total_sum

main()
