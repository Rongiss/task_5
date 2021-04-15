
CONST_AREA = 10
#СONST_PRICE_COLOR = 35
CONST_WORK_TIME = 8
PRICE_COMPANY = 2000

def main():
    color_price = input_price_color()
    area_working = input_area_for_work()



def input_area_for_work():
    print('\nВведите площадь для  покраски')
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



main()
