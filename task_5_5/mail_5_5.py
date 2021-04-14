
CONST_PECENT = 0.6

def main_5_5():
    start_message()
    calculate(input_function())
    out_message()

def start_message():
    print('{0:*^45}'.format('*'))
    print('{0:*^45}'.format(' Программа налога на недвижемость '))
    print('{0:*^45}'.format('*'))



def input_function():
    print('\nВведим сумму фактической стоимости недвижемости $', end='')
    cash_from_user = float(input())
    while cash_from_user < 0:
        print('Сумма не может быть меньше нуля!')
        print('Повторите ввод данных')
        print('\nВведим сумму фактической стоимости недвижемости $', end='')
    return cash_from_user

def calculate(cash):
    ocan_st = cash * CONST_PECENT
    tax = ocan_st * 0.0072
    print('\n{0:_^45}'.format('_'))
    print('Оценочная стоимость равна -', format(ocan_st, '.2f'), sep=' ')
    print('Налог на имущество составляет -', format(tax, '.2f'), sep=' ')
    print('{0:_^45}'.format('_'))

def out_message():
    print('\n{0:*^45}'.format('*'))
    print('{0:*^45}'.format(' Программа закончилась '))
    print('{0:*^45}'.format('*'))


main_5_5()