import math
def calcalculete_and_out(fed_tax, reg_tax, cash):
    fed_tax /= 100
    reg_tax /= 100
    cash_fed_tax = cash * fed_tax
    cash_reg_tax = cash * reg_tax

    print('{0:_^45}'.format(''))
    print('\nСумма покаупки - {}'.format(cash, '.2f'))
    print('Федеральный налог за покаупку составляет -', format(cash_fed_tax, '.2f'))
    print('Региональный налог за покаупку составляет -', format(cash_reg_tax, '.2f'))
    print('Итоговая сумма составляет - ', format((cash + cash_reg_tax + cash_fed_tax), '.2f'))
    print('{0:_^45}'.format(''))
