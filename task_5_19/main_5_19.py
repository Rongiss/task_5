def main():
    cash = 1000#float(input('Количество средств на счете - '))
    mounth = 12#int(input('Количество месяцев - '))
    pecent = 0.05#float(input('Процунтная ставка - '))

    print('\nБудующая сумма равна -', format(result(cash,mounth, pecent), '.2f'))

def result(cash,mounth, pecent):
    result_all = cash
    p = cash * ((1 + pecent) ** mounth)
    return p

main()