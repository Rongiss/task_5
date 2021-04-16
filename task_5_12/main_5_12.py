def main_5_12():
    num1 = int(input('Введите первое число -'))
    num2 = int(input('Введите второе число -'))
    print('\nНаибольшее число -', max(num1, num2), sep=' ')

def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


main_5_12()