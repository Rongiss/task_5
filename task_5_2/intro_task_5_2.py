# Функция приветственного сообщения
def info(fed_tax, reg_tax):
    print('{0:*^45}'.format(''))
    print('{0:-^45}'.format('Программа подсчета суммы покупки'))
    print('{0:*^45}'.format(''))

    print('\nНа данный момент:')
    print('\nФедеральный налог составляет - {}%'.format(fed_tax))
    print('Региональный налог составляет - {}%'.format(reg_tax))
    print('{0:_^45}'.format(''))

# Функция завершающего сообщения
def out_list():

    print('\n{0:*^45}'.format(''))
    print('{0:-^45}'.format('Всего Вам хорошего'))
    print('{0:*^45}'.format(''))


