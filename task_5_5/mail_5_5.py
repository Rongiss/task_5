
# Константы процентной ставки
# Константа оценочной стоимости
CONST_PECENT = 0.6
# Константа налоговой ставки
CONST_TAX = 0.0072

# главная функция
def main_5_5():
    # Вызов функции приветсвенного сообщения
    start_message()

    # Вызов функции расчета налога с полученным
    # Значением функции ввдо данных
    calculate(input_function())
    # Функуия вывода сообщения о завершении
    out_message()

# Объявление функции приветсвенного сообщения
def start_message():
    print('{0:*^45}'.format('*'))
    print('{0:*^45}'.format(' Программа налога на недвижемость '))
    print('{0:*^45}'.format('*'))


# Объявление функции ввода данных пользователем
def input_function():
    print('\nВведим сумму фактической стоимости недвижемости $', end='')
    cash_from_user = float(input())
    # Валидация введенных данных
    while cash_from_user < 0:
        print('Сумма не может быть меньше нуля!')
        print('Повторите ввод данных')
        print('\nВведим сумму фактической стоимости недвижемости $', end='')
    # Возвращаяемое значение функцией для передачи
    return cash_from_user

# Объявление функции расчета налога
def calculate(cash):
    # Переменная оценочной стоимости
    ocan_st = cash * CONST_PECENT
    # Переменная налоговой ставки
    tax = ocan_st * CONST_TAX
    # Вывод информации
    print('\n{0:_^45}'.format('_'))
    print('Оценочная стоимость равна -', format(ocan_st, '.2f'), sep=' ')
    print('Налог на имущество составляет -', format(tax, '.2f'), sep=' ')
    print('{0:_^45}'.format('_'))
# Объявление функуии вывода сообщения о завершении
def out_message():
    print('\n{0:*^45}'.format('*'))
    print('{0:*^45}'.format(' Программа закончилась '))
    print('{0:*^45}'.format('*'))

# Вызов главной функции
main_5_5()