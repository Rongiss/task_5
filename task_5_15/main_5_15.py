
def main():
    total = 0
    how_many = int(input('Введите количество предметов - '))
    for i in range(how_many):
        ocen = int(input('\nВведите оценку - '))
        while ocen < 0:
            print('\nВы ошиблись и ввели отрицательное значение')
            print("Поторите попытку")
            ocen = int(input('Введите оценку - '))
        total += ocen
        print('It is - ', determain_grange(ocen))

    print('\nСредний бал - ', format(calc_average(total, how_many), '.2f'))

def calc_average(total, how_many):
    return total / how_many


def determain_grange(oc):
    if oc < 60:
        res = 'F'
    elif oc >= 60 and oc < 70:
        res = 'D'
    elif oc >= 70 and oc < 80:
        res = "C"
    elif oc >= 80 and oc < 90:
        res = 'B'
    else:
        res = 'A'
    return res



main()