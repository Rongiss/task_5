
def main():

    futt = float(input('\nВведите количество футов '))

    while futt < 0:
        print('\nВы ввели отрицательное значние')
        print("Значение должно быть больше или равно нулю")
        print("Поторите попытку")
        futt = float(input('Введите количество футов '))

    duim, say = feet_to_inches(futt)

    print('\nВ {} содержиться {} {}'.format(futt, duim, say))


def feet_to_inches(futt):
    duim = futt * 12
    if duim == 0 or duim % 10:
        say = 'дюймов'
    elif duim == 1 or duim % 10 and duim != 11:
        say = 'дюйм'
    elif duim % 10 == 2 and duim !=12 or \
        duim % 10 == 3 and duim != 13 or \
        duim % 10 == 4 and duim != 14:
        say = 'дюйма'
    else:
        say = 'дюймов'


    return duim, say
main()
