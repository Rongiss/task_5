def enter_cash():
    print('\nЗдраствуйте, мы рады приветствовать Вас!')
    print('{0:_^45}'.format(''))
    cash = float(input('\nВведите сумм покупки - '))

    while cash < 0:
        print()
        print('{0:*^45}'.format(''))
        print('{0:*^45}'.format('  Сумма не может быть отрицательной  '))
        print('{0:*^45}'.format('  Введите сумму еще раз  '))
        print('{0:*^45}'.format(''))
        cash = float(input('\nВведите сумм покупки - '))


    return cash